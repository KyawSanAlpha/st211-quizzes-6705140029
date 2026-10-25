| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Function Parametrization

## Overview

This folder demonstrates testing small mathematical utility functions against multiple input and expected-result pairs using pytest parametrization.

## Files

| File | Description |
| :--- | :--- |
| [mathutils.py](./mathutils.py) | Defines `is_even` and `factorial`. `factorial` raises `ValueError` for negative input. |
| [test_factorial.py](./test_factorial.py) | Checks factorial results for values from 0 through 5. |
| [test_param.py](./test_param.py) | Checks `is_even` against several even and odd numbers. |

## Key concept

Each parameter value or input/expected-result tuple is run as its own test case. These tests cover regular non-negative factorial inputs and both even and odd integer inputs for `is_even`.

## Run

From the `Lab_05` directory:

```powershell
python -m pytest .\Parametrization -q
```
