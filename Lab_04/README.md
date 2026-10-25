| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Lab 04 - Pytest Fixtures

## Overview

This lab demonstrates pytest fixtures and the ways they help prepare, reuse, and clean up test data. The examples cover fixture factories, ordinary fixtures, fixtures shared between test modules, fixture scopes, and setup/teardown patterns.

## Folder structure

| Folder | Topic |
| :--- | :--- |
| [Factory_Fixtures](./Factory_Fixtures/README.md) | Fixture factories that create test data on demand |
| [Fixtures](./Fixtures/README.md) | Basic fixtures for reusable test objects |
| [Fixtures_Shares](./Fixtures_Shares/README.md) | Fixtures shared by multiple test modules through `conftest.py` |
| [Scopes](./Scopes/README.md) | Function, module, and session fixture scopes |
| [SetUp&Teardown](./SetUp%26Teardown/README.md) | Resource setup and cleanup with yield fixtures |

## Requirements

- Python
- pytest

Install pytest if it is not available in the active environment:

```powershell
python -m pip install pytest
```

## Run the tests

From this `Lab_04` directory, run the complete lab test suite:

```powershell
python -m pytest -q
```

Run one topic at a time by specifying its folder. For example:

```powershell
python -m pytest .\Factory_Fixtures -q
```

## Current validation and notes

The current suite completes with **20 passed** when run from the `Lab_04` directory.

The bank-account examples reject non-positive deposits and withdrawals that exceed the balance, but their `withdraw` methods do not reject negative amounts. The `test_multiple_accounts` example creates two accounts without asserting their state. These are limitations of the current examples, not guarantees of the behavior they demonstrate.

The file teardown example writes to `test_data.txt` in the current working directory and removes it during teardown. Avoid running it from a directory where that filename contains data you need to keep.
