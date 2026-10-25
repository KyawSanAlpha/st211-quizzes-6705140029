| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Test IDs and Readability

## Overview

This folder demonstrates how pytest names parameterized test cases, how to provide custom IDs for clearer test output, and how to use parameter marks.

## Files

| File | Description |
| :--- | :--- |
| [test_defalut_ids.py](./test_defalut_ids.py) | Uses pytest's automatically generated IDs for parameter values containing user data. |
| [test_custom_ids.py](./test_custom_ids.py) | Assigns explicit IDs (`alice-adult` and `bob-adult`) to parameter cases. |
| [test_param_ids.py](./test_param_ids.py) | Uses `pytest.param` to assign descriptive IDs to discount cases. |
| [test_param_marks.py](./test_param_marks.py) | Uses `pytest.param` with IDs to label square-calculation cases. |

## Run

From the `Lab_05` directory:

```powershell
python -m pytest '.\Ids&Readibility' -q
```

## Current note

`test_param_ids.py` imports `apply_discount` from `discount`, but this folder does not contain a `discount.py` module. The existing implementation is in the sibling `Parameters` folder, so this test currently fails to import when collected.
