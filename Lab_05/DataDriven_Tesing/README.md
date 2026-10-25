| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Data-Driven Testing

## Overview

This folder demonstrates parameterizing tests from external test data stored in CSV and JSON files. Pytest uses the loaded rows or objects as test inputs, allowing the same test function to check multiple cases.

## Files

| File | Description |
| :--- | :--- |
| [login.csv](./login.csv) | Login inputs and expected validity values, with `username`, `password`, and `valid` columns. |
| [test_cases.json](./test_cases.json) | JSON input/expected-value pairs used by the uppercase test. |
| [validate.py](./validate.py) | Defines `is_valid_login`, which returns true when both username and password are non-empty. |
| [test_csv_driven.py](./test_csv_driven.py) | Loads login rows from the CSV file and checks them against `is_valid_login`. |
| [test_data_driven.py](./test_data_driven.py) | Loads JSON test cases and checks that each input is converted to uppercase. |

## Run

From the `Lab_05` directory:

```powershell
python -m pytest '.\DataDriven_Tesing' -q
```

## Current notes

- `test_csv_driven.py` reads `login.csv` relative to its own file.
- `test_data_driven.py` currently opens `test_cases.json` relative to the current working directory. Run from this folder for that file to be found.
- The last JSON case has numeric input `1`, but the test calls `.upper()` on every input. That case raises `AttributeError`; the test expects strings.
