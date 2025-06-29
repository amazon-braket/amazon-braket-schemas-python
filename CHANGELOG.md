# Changelog

## v1.24.2 (2025-06-25)

### Bug Fixes and Other Changes

 * updating IonQ device capability schema to include standardized property

## v1.24.1 (2025-06-23)

### Bug Fixes and Other Changes

 * Add standardized gate model QPU device properties v3

## v1.24.0 (2025-04-29)

### Features

 * add standardized v2

## v1.23.3 (2025-03-24)

### Bug Fixes and Other Changes

 * style: update linter to use UP rules

## v1.23.2 (2025-03-08)

### Bug Fixes and Other Changes

 * Use builtins for type hints

## v1.23.1 (2025-01-28)

### Bug Fixes and Other Changes

 * constrain device connectivitiy

## v1.23.0 (2025-01-15)

### Features

 * add rigetti device properties v2 schemas

## v1.22.4 (2024-12-09)

### Bug Fixes and Other Changes

 * Clarify the meaning of aggregate performance metrics in the quera device schema

## v1.22.3 (2024-11-07)

### Bug Fixes and Other Changes

 * clarify the meaning of PerformanceRydbergLocal attributes

## v1.22.2 (2024-11-04)

### Bug Fixes and Other Changes

 * Refactoring `jaqcd.results` and `jaqcd.shared_models` to use `gate_model_shared` instead.

## v1.22.1 (2024-09-24)

### Bug Fixes and Other Changes

 * update xanadu tests to use with pytest.raise

## v1.22.0 (2024-05-22)

### Features

 * add iqm schemas

## v1.21.4 (2024-04-15)

### Bug Fixes and Other Changes

 * add Rydberg local schemas

## v1.21.3 (2024-04-10)

### Bug Fixes and Other Changes

 * add local detuning export

## v1.21.2 (2024-04-10)

### Bug Fixes and Other Changes

 * change shiftingFields to localDetuning

## v1.21.1 (2024-04-01)

### Bug Fixes and Other Changes

 * restore dependent tests after the Pydantic migration

## v1.21.0 (2024-03-27)

### Features

 * move to Pydantic 2.0 and use the 1.10 patch branch

## v1.20.2 (2024-02-07)

### Bug Fixes and Other Changes

 * update quera_ahs_paradigm doc string

## v1.20.1 (2024-01-31)

### Bug Fixes and Other Changes

 * formatting for RydbergGlobal doc string

## v1.20.0 (2024-01-30)

### Features

 * add performance schema for Aquila

## v1.19.1.post0 (2023-09-14)

### Documentation Changes

 * Replace aws org with amazon-braket
 * change the sphinx requirement to be greater than 7.0.0

## v1.19.1 (2023-07-25)

### Bug Fixes and Other Changes

 * Specify waveform types

## v1.19.0 (2023-07-12)

### Features

 * add the native gate calibration schema

## v1.18.0 (2023-06-29)

### Features

 * add support for python 3.11

## v1.17.0 (2023-05-16)

### Features

 * Introduce error mitigation

## v1.16.1 (2023-05-12)

### Bug Fixes and Other Changes

 * constrain modifier name string

## v1.16.0 (2023-05-11)

### Features

 * supportedModifiers schema

## v1.15.1 (2023-05-03)

### Bug Fixes and Other Changes

 * test: parallelize test execution for pytest

## v1.15.0 (2023-03-03)

### Deprecations and Removals

 * deprecate python 3.7

### Documentation Changes

 * Remove Black badge

## v1.14.1.post0 (2023-02-13)

### Testing and Release Infrastructure

 * update github workflows for node12 retirement

## v1.14.1 (2023-02-09)

### Bug Fixes and Other Changes

 * update: adding build for python 3.10

## v1.14.0 (2022-12-07)

### Features

 * adjoint gradient

## v1.13.1.post1 (2022-11-23)

### Documentation Changes

 * remove ir types from examples

## v1.13.1.post0 (2022-11-21)

### Testing and Release Infrastructure

 * Remove Ocean plugin from dependent tests

## v1.13.1 (2022-11-16)

### Bug Fixes and Other Changes

 * Reference code from the current commit for dependent tests

## v1.13.0 (2022-11-14)

### Features

- add getTaskPollIntervalMillis to device service properties

## v1.12.0 (2022-10-31)

### Features

- support new device schema quera and new ir schema ahs

## v1.11.0 (2022-10-20)

### Features

- Add support for pulses

## v1.10.2 (2022-08-25)

### Bug Fixes and Other Changes

- Removing unused OpenQASM3 results schema

## v1.10.1.post0 (2022-08-10)

### Testing and Release Infrastructure

- Add feature branch pull request tests
- Add SF plugin to dependent tests

## v1.10.1 (2022-08-04)

### Bug Fixes and Other Changes

- OpenQASM Local Simulator support

## v1.10.0 (2022-06-02)

### Features

- Add support for photonic computations

## v1.9.0 (2022-04-06)

### Features

- Add standardized device calibration data for OQC and Rigetti

## v1.8.0 (2022-03-07)

### Features

- Add support for running OpenQASM programs

## v1.7.2 (2022-02-27)

### Bug Fixes and Other Changes

- Oqc release

## v1.7.1 (2022-02-01)

### Bug Fixes and Other Changes

- multiqubit pauli channel with multitarget

## v1.7.0 (2022-02-01)

### Features

- adding MultiQubitPauliChannel to ir

### Bug Fixes and Other Changes

- Relax requirements from pydantic

## v1.6.0 (2022-01-27)

### Features

- add control-sqrt-not gate

## v1.5.1 (2022-01-04)

### Bug Fixes and Other Changes

- change annealingDurationRange to a list of floats.

## v1.5.0 (2021-11-29)

### Features

- Add support for jobs

## v1.4.1 (2021-09-30)

## v1.4.0.post0 (2021-09-10)

### Documentation Changes

- Fix jaqcd typo in README.md

## v1.4.0 (2021-09-02)

### Features

- StartVerbatimBox and EndVerbatimBox

### Bug Fixes and Other Changes

- Update copyright headers

## v1.3.0 (2021-08-05)

### Features

- support for StartPreserveBlock and EndPreserveBlock instructions.

## v1.2.2 (2021-06-04)

### Bug Fixes and Other Changes

- fix d-wave schema constraints

## v1.2.1 (2021-05-26)

### Bug Fixes and Other Changes

- Add schema helper methods, modify device level tests, and fix some docs

## v1.2.0 (2021-05-24)

### Features

- Noise operators

### Bug Fixes and Other Changes

- Revert "fix: change documentation for deviceLevelParameters (#86)"
- change documentation for deviceLevelParameters

### Testing and Release Infrastructure

- tox for GitHub checks

## v1.1.4 (2021-05-11)

### Bug Fixes and Other Changes

- allow null values to be passed in for optional parameters

## v1.1.3 (2021-04-16)

### Bug Fixes and Other Changes

- move device-specific schemas into their own files

## v1.1.2 (2021-04-15)

### Bug Fixes and Other Changes

- error message typo

## v1.1.1 (2021-03-26)

### Bug Fixes and Other Changes

- add device level parameters and device-specific parameters

## v1.1.0.post6 (2021-03-19)

### Testing and Release Infrastructure

- Run unit tests for dependent packages

## v1.1.0.post5 (2021-03-11)

### Testing and Release Infrastructure

- Add Python 3.9

## v1.1.0.post4 (2021-03-03)

### Testing and Release Infrastructure

- Make python-package consistent with other repos

## v1.1.0.post3 (2021-03-01)

### Documentation Changes

- fix time unit for D-Wave metadata from milliseconds to microseconds

## v1.1.0.post2 (2021-01-06)

### Testing and Release Infrastructure

- Add CodeCov badge
- Upload coverage report to Codecov

## v1.1.0.post1 (2020-12-30)

### Testing and Release Infrastructure

- Add build badge
- Use GitHub Actions for CI

## v1.1.0.post0 (2020-12-04)

### Testing and Release Infrastructure

- Make tox commands consistent with other repos

## v1.1.0 (2020-11-23)

### Features

- Add explicit qubit allocation

## v1.0.3 (2020-11-03)

### Bug Fixes and Other Changes

- Feature/lower latency

## v1.0.2.post2 (2020-10-30)

### Testing and Release Infrastructure

- updating codeowners

## v1.0.2.post1 (2020-09-10)

### Testing and Release Infrastructure

- fix black formatting

## v1.0.2.post0 (2020-09-09)

### Testing and Release Infrastructure

- Add CHANGELOG.md

## v1.0.2 (2020-09-04)

## Bug Fixes

- Update the schema validation for GateModelParameters to be more strict, this will avoid Pydantic to auto convert String integers to int.

## v1.0.1 (2020-08-25)

## Bug Fixes

- Update the Rigetti task result schema to allow for the program duration to be zero.

## v1.0.0.post1 (2020-08-14)

The only way to update a description in PyPi is to upload new files;
however, uploading an existing version is prohibited. The recommended
way to deal with this is with
[post-releases](https://www.python.org/dev/peps/pep-0440/#post-releases).

## v1.0.0 (2020-08-13)

This is the public release of the Amazon Braket Python Schemas!

Amazon Braket Python Schemas is an open source library that contains the schemas for Braket, including:

- intermediate representations (IR) for Amazon Braket quantum tasks and offers serialization and deserialization of those IR payloads. Think of the IR as the contract between the Amazon Braket SDK and Amazon Braket API for quantum programs.
- schemas for the S3 results of each quantum task
- schemas for the device capabilities of each device
