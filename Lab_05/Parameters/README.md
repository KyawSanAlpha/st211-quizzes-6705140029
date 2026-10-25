| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Parameterized Test Cases

## Overview

This folder demonstrates using `pytest.mark.parametrize` to test normal results, invalid inputs, and combinations of multiple parameters.

## Files

| File | Description |
| :--- | :--- |
| [discount.py](./discount.py) | Defines `apply_discount`, which calculates a discounted price and raises `ValueError` for percentages outside 0–100. |
| [test_discount.py](./test_discount.py) | Checks discount calculations using several price/percentage/expected-result combinations. |
| [test_discount_errors.py](./test_discount_errors.py) | Checks that invalid discount percentages raise `ValueError`. |
| [test_multi.py](./test_multi.py) | Uses two parameter decorators to test the Cartesian product of `x` and `y` values. |

## Key concept

Each row supplied to `parametrize` becomes a separate test case. Applying multiple parameter decorators creates combinations of their values; this example checks six `x`/`y` pairs.

## Run

From the `Lab_05` directory:

```powershell
python -m pytest .\Parameters -q
```
