| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Lab 05 - Parametrized Testing

## Overview

This lab demonstrates ways to run tests with multiple inputs using pytest parametrization, readable test IDs, parameterized fixtures, and external test data in CSV and JSON files.

## Folder structure

| Folder | Topic |
| :--- | :--- |
| [DataDriven_Tesing](./DataDriven_Tesing/) | Loading test cases from CSV and JSON data files. |
| [Ids&Readibility](<./Ids&Readibility/>) | Using default, custom, and parameter-based test IDs, plus marks. |
| [Parameterized_Fixtures](./Parameterized_Fixtures/) | Running tests repeatedly with fixture-provided parameters. |
| [Parameters](./Parameters/) | Parametrizing function inputs, expected results, errors, and input combinations. |
| [Parametrization](./Parametrization/) | Testing math utility functions with multiple input values. |

## Requirements

- Python
- pytest

Install pytest if it is not available in the active environment:

```powershell
python -m pip install pytest
```

## Run the tests

From this `Lab_05` directory, run all tests:

```powershell
python -m pytest -q
```

Run a single topic folder:

```powershell
python -m pytest .\Parameterized_Fixtures -q
```

For a folder name containing `&`, quote the path in PowerShell:

```powershell
python -m pytest '.\Ids&Readibility' -q
```

## Current status and known issues

The topic folders were checked individually. `Parameterized_Fixtures` passed **9 tests**, `Parameters` passed **16 tests**, and `Parametrization` passed **16 tests**. `DataDriven_Tesing` had **8 passing tests and 1 failure**. `Ids&Readibility` has a test-collection import error.

The current data-driven examples have two issues:

- `test_data_driven.py` opens `test_cases.json` relative to the current working directory, so running the suite from the `Lab_05` root can fail to find the file.
- One JSON case supplies a number to a test that calls `.upper()`, causing an `AttributeError`.

In `Ids&Readibility`, `test_param_ids.py` imports `apply_discount` from `discount`, but that module is not in the same folder. The existing `discount.py` is in the sibling `Parameters` folder.

These issues are documented as-is; this README does not change or correct the test examples.
