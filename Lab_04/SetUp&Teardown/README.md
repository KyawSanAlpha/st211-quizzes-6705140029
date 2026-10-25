| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Setup and Teardown

## Purpose

This folder demonstrates preparing resources before a test and releasing or cleaning them after the test, using pytest fixtures that yield a value.

## Files

| File | Description |
| :--- | :--- |
| [test_db_style.py](./test_db_style.py) | Uses a fake database object and a yield fixture to connect before the test and disconnect afterward. |
| [test_teardown.py](./test_teardown.py) | Creates a text file for each test, yields its filename, and removes the file during fixture teardown. |

## Key concept

When a fixture uses `yield`, the value before `yield` is provided to the test. After the test completes, pytest resumes the fixture after `yield`, allowing cleanup to run.

## Run

From the `Lab_04` directory:

```powershell
python -m pytest '.\SetUp&Teardown' -q
```

## Important file-handling note

`test_teardown.py` uses the fixed filename `test_data.txt` relative to the process's current working directory. It opens that path for writing and then removes it during teardown. Run the test only from a directory where overwriting and deleting that filename is safe.
