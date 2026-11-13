# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

"""Report schema changes between two source trees that break payload compatibility.

Usage: python schema_compatibility.py BASE_SRC HEAD_SRC
"""

import importlib
import inspect
import json
import subprocess
import sys
import warnings
from collections import defaultdict
from pathlib import Path

PACKAGES = (
    "braket.device_schema",
    "braket.ir",
    "braket.jobs_data",
    "braket.schema_common",
    "braket.task_result",
)
IGNORED = {"title", "description", "examples"}
HANDLED = {
    "properties",
    "required",
    "items",
    "additionalProperties",
    "anyOf",
    "oneOf",
    "allOf",
    "default",
    "enum",
}


def dump(src: str) -> dict:
    """Return the import paths and JSON schema of every model in `src`."""
    warnings.filterwarnings("ignore")
    sys.path.insert(0, src)
    from pydantic import BaseModel
    from pydantic.v1 import BaseModel as BaseModelV1

    paths, schemas, public = {}, {}, set()
    for file in sorted(Path(src, "braket").rglob("*.py")):
        parts = file.relative_to(src).with_suffix("").parts
        module_name = ".".join(parts[:-1] if parts[-1] == "__init__" else parts)
        if not module_name.startswith(PACKAGES):
            continue
        module = importlib.import_module(module_name)
        for name, obj in vars(module).items():
            if name.startswith("_") or not inspect.isclass(obj):
                continue
            if not issubclass(obj, (BaseModel, BaseModelV1)) or obj in (BaseModel, BaseModelV1):
                continue
            if not obj.__module__.startswith(PACKAGES):
                continue
            canonical = f"{obj.__module__}.{obj.__qualname__}"
            paths[f"{module_name}.{name}"] = canonical
            if obj.__module__ == module_name or parts[-1] == "__init__":
                public.add(f"{module_name}.{name}")
            if canonical not in schemas:
                v1 = issubclass(obj, BaseModelV1)
                schemas[canonical] = (
                    json.loads(obj.schema_json()) if v1 else obj.model_json_schema()
                )
    return {"paths": paths, "public": sorted(public), "schemas": schemas}


def load(src: str) -> dict:
    result = subprocess.run(
        [sys.executable, "-I", __file__, "--dump", src],
        check=True,
        stdout=subprocess.PIPE,
        text=True,
    )
    return json.loads(result.stdout)


def resolve(node, defs: dict, stack: frozenset = frozenset()):
    """Inline `$ref` targets so renamed but identical models compare equal."""
    if isinstance(node, list):
        return [resolve(item, defs, stack) for item in node]
    if not isinstance(node, dict):
        return node
    if "$ref" in node:
        name = node["$ref"].split("/")[-1]
        if name in stack:
            return {"recursiveRef": name}
        return resolve(defs.get(name, {}), defs, stack | {name})
    return {
        key: resolve(value, defs, stack)
        for key, value in node.items()
        if key not in IGNORED and key not in ("definitions", "$defs")
    }


def short(value) -> str:
    text = json.dumps(value, sort_keys=True)
    return text if len(text) <= 120 else text[:117] + "..."


def options(node: dict) -> list:
    for key in ("anyOf", "oneOf"):
        if key in node:
            return node[key]
    return [node]


def compare_options(old: list, new: list, path: str):
    keys_old = [json.dumps(item, sort_keys=True) for item in old]
    keys_new = [json.dumps(item, sort_keys=True) for item in new]
    lost = [item for item, key in zip(old, keys_old) if key not in keys_new]
    gained = [item for item, key in zip(new, keys_new) if key not in keys_old]
    if len(lost) == 1 and len(gained) == 1:
        yield from walk(lost[0], gained[0], path)
        return
    if lost:
        yield path, f"union lost {len(lost)} option(s); existing payloads may no longer parse"
    if gained:
        yield path, f"union gained {len(gained)} option(s); older releases reject new payloads"
    if not lost and not gained and keys_old != keys_new:
        yield path, "union options reordered; payloads may parse as a different type"


def walk(old, new, path: str):
    if old == new:
        return
    if not isinstance(old, dict) or not isinstance(new, dict):
        yield path, f"changed from {short(old)} to {short(new)}"
        return
    yield from compare_default(old, new, path)
    if any(key in old or key in new for key in ("anyOf", "oneOf")):
        yield from compare_options(options(old), options(new), path)
        return
    yield from compare_fields(old, new, path)
    if len(old.get("allOf", [])) == 1 and len(new.get("allOf", [])) == 1:
        yield from walk(old["allOf"][0], new["allOf"][0], path)
    elif old.get("allOf") != new.get("allOf"):
        yield path, f"allOf changed from {short(old.get('allOf'))} to {short(new.get('allOf'))}"
    for key, suffix in (("items", "[]"), ("additionalProperties", "{}")):
        if isinstance(old.get(key), dict) and isinstance(new.get(key), dict):
            yield from walk(old[key], new[key], path + suffix)
        elif old.get(key) != new.get(key):
            yield path, f"{key} changed from {short(old.get(key))} to {short(new.get(key))}"
    if "enum" in old or "enum" in new:
        yield from compare_enum(old.get("enum", []), new.get("enum", []), path)
    for key in sorted((old.keys() | new.keys()) - HANDLED):
        if old.get(key) != new.get(key):
            yield path, f"{key} changed from {short(old.get(key))} to {short(new.get(key))}"


def compare_fields(old: dict, new: dict, path: str):
    old_props, new_props = old.get("properties", {}), new.get("properties", {})
    old_req, new_req = set(old.get("required", [])), set(new.get("required", []))
    for field in sorted(old_props.keys() - new_props.keys()):
        yield f"{path}.{field}", "field removed"
    for field in sorted(new_props.keys() - old_props.keys()):
        if field in new_req:
            yield f"{path}.{field}", "required field added; existing payloads no longer parse"
    for field in sorted((new_req - old_req) & old_props.keys()):
        yield f"{path}.{field}", "field became required; existing payloads may no longer parse"
    for field in sorted((old_req - new_req) & new_props.keys()):
        yield f"{path}.{field}", "field became optional; older releases reject payloads without it"
    for field in sorted(old_props.keys() & new_props.keys()):
        yield from walk(old_props[field], new_props[field], f"{path}.{field}")


def compare_default(old: dict, new: dict, path: str):
    if "default" in old and "default" in new and old["default"] != new["default"]:
        yield path, f"default changed from {short(old['default'])} to {short(new['default'])}"


def compare_enum(old: list, new: list, path: str):
    lost = [value for value in old if value not in new]
    gained = [value for value in new if value not in old]
    if lost:
        yield path, f"enum lost {short(lost)}; existing payloads no longer parse"
    if gained:
        yield path, f"enum gained {short(gained)}; older releases reject new payloads"


def definitions(schema: dict) -> dict:
    return schema.get("definitions", schema.get("$defs", {}))


def compare(base: dict, head: dict) -> dict:
    """Return findings grouped by message, each with the affected models and fields."""
    findings = defaultdict(list)
    for path in sorted(set(base["public"]) - head["paths"].keys()):
        findings["model no longer importable"].append(path)
    pairs = {}
    for path, canonical in base["paths"].items():
        if path in head["paths"]:
            pairs.setdefault(canonical, head["paths"][path])
    for old_name, new_name in sorted(pairs.items()):
        old_schema, new_schema = base["schemas"][old_name], head["schemas"][new_name]
        old_resolved = resolve(old_schema, definitions(old_schema))
        new_resolved = resolve(new_schema, definitions(new_schema))
        label = new_name.removeprefix("braket.")
        for path, message in walk(old_resolved, new_resolved, label):
            if path not in findings[message]:
                findings[message].append(path)
    return findings


def main() -> int:
    if sys.argv[1] == "--dump":
        json.dump(dump(sys.argv[2]), sys.stdout)
        return 0
    findings = compare(load(sys.argv[1]), load(sys.argv[2]))
    if not findings:
        print("No incompatible schema changes found.")
        return 0
    for message, paths in sorted(findings.items()):
        print(message)
        for path in paths:
            print(f"    {path}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
