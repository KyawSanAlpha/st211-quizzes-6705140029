| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Parameterized Fixtures

## Overview

This folder demonstrates pytest fixtures with a `params` list. Pytest runs each test that requests a parameterized fixture once for each configured value.

## Files

| File | Description |
| :--- | :--- |
| [test_browser.py](./test_browser.py) | Supplies `chrome`, `firefox`, and `safari` through a fixture and prints setup/teardown messages for each value. Two tests use the fixture. |
| [test_param_fixture.py](./test_param_fixture.py) | Supplies `sqlite`, `postgresql`, and `mysql` through a fixture and checks each parameter value. |

## Key concept

The special pytest `request` fixture provides the current parameter as `request.param`. With three browser values and two tests using the browser fixture, pytest creates six browser test cases. The database fixture has three parameter values and creates three cases for its test.

## Run

From the `Lab_05` directory:

```powershell
python -m pytest .\Parameterized_Fixtures -q
```

The example browser fixture uses browser-name strings only; it does not launch real browser software.
