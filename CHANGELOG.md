# Changelog

## v1.0.2 (2020-09-04)

## Bug Fixes

* Update the schema validation for GateModelParameters to be more strict, this will avoid Pydantic to auto convert String integers to int.

## v1.0.1 (2020-08-25)

## Bug Fixes

* Update the Rigetti task result schema to allow for the program duration to be zero.

## v1.0.0.post1 (2020-08-14)

The only way to update a description in PyPi is to upload new files;
however, uploading an existing version is prohibited. The recommended
way to deal with this is with
[post-releases](https://www.python.org/dev/peps/pep-0440/#post-releases).

## v1.0.0 (2020-08-13)

This is the public release of the Amazon Braket Python Schemas!

Amazon Braket Python Schemas is an open source library that contains the schemas for Braket, including:
* intermediate representations (IR) for Amazon Braket quantum tasks and offers serialization and deserialization of those IR payloads. Think of the IR as the contract between the Amazon Braket SDK and Amazon Braket API for quantum programs.
* schemas for the S3 results of each quantum task
* schemas for the device capabilities of each device