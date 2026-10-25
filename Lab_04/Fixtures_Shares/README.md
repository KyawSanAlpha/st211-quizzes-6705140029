| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Shared Fixtures

## Purpose

This folder demonstrates how a `conftest.py` file makes fixtures available to multiple test modules in the same test directory without importing the fixtures into each test file.

## Files

| File | Description |
| :--- | :--- |
| [bank.py](./bank.py) | Defines the `BankAccount` example class. |
| [conftest.py](./conftest.py) | Defines shared fixtures for empty and funded accounts and a sample user list. |
| [test_shared_a.py](./test_shared_a.py) | Tests the account fixtures. |
| [test_shared_b.py](./test_shared_b.py) | Tests the sample-user fixture and a funded account withdrawal. |

## Key concept

Pytest discovers `conftest.py` automatically. Fixtures defined there are available to test modules beneath the same directory, including both `test_shared_a.py` and `test_shared_b.py`. The `empty_account`, `funded_account`, and `sample_users` fixtures each return their own prepared value.

## Run

From the `Lab_04` directory:

```powershell
python -m pytest .\Fixtures_Shares -q
```

## Note

The example `BankAccount.withdraw` method does not validate that the withdrawal amount is positive.
