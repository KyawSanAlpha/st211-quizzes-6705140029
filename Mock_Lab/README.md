| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Mock Lab - Testing Weather Descriptions

## Overview

This exercise demonstrates why tests that depend on random values can be unreliable and how mocking controls a dependency to make tests deterministic.

The `weather` module generates a random temperature and maps it to a description:

| Temperature in Celsius | Description |
| :--- | :--- |
| Below 0 | `Freezing` |
| 0 to 14 | `Cold` |
| 15 to 24 | `Pleasant` |
| 25 and above | `Hot` |

## Files

| File | Description |
| :--- | :--- |
| [weather.py](./weather.py) | Defines `get_temperature`, which returns a random value from -10 to 40, and `describe_weather`, which returns a description for that value. |
| [test_problem.py](./test_problem.py) | Demonstrates a weak test that checks only whether the random result belongs to the list of valid descriptions. |
| [test_solution.py](./test_solution.py) | Patches `weather.get_temperature` to provide fixed temperatures and checks each description branch deterministically. |

## Why mock the dependency?

`test_problem.py` relies on a random temperature. Its assertion can pass without checking that every temperature range maps to the correct description, and the test does not control which branch is exercised.

`test_solution.py` uses `unittest.mock.patch` to replace `get_temperature` with a known value for each test. This makes each expected result reproducible and lets the tests directly verify all four conditions.

## Run

From the repository root:

```powershell
python -m pytest Mock_Lab -q
```

To run only the deterministic mock-based tests:

```powershell
python -m pytest Mock_Lab\test_solution.py -q
```
