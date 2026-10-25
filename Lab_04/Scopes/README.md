| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Fixture Scopes

## Purpose

This folder compares fixture scopes and shows how fixture scope controls how often pytest creates a fixture value during a test run.

## Files

| File | Description |
| :--- | :--- |
| [test_scope.py](./test_scope.py) | Compares a function-scoped fixture with a module-scoped fixture across tests in one module. |
| [test_session.py](./test_session.py) | Demonstrates a session-scoped fixture reused by multiple tests. |

## Scope summary

| Scope | Fixture lifetime |
| :--- | :--- |
| `function` | Created separately for each test that requests it. |
| `module` | Reused by tests in the same test module. |
| `session` | Reused throughout a pytest test session. |

## Run

From the `Lab_04` directory:

```powershell
python -m pytest .\Scopes -q
```

## Note

In `test_scope.py`, `test_three` currently uses `assert True`; this assertion always passes and does not check a fixture value. The other tests in that file do verify the returned fixture values.
