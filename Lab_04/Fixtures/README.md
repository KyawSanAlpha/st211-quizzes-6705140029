| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Basic Fixtures

## Purpose

This folder introduces a simple pytest fixture that prepares a reusable object for each test that requests it.

## Files

| File | Description |
| :--- | :--- |
| [bank.py](./bank.py) | Defines the `BankAccount` example class. |
| [test_after.py](./test_after.py) | Provides an `account` fixture initialized with a balance of 100 and tests deposit and withdrawal behavior. |

## Key concept

The `@pytest.fixture` decorator marks `account` as a fixture. Pytest injects its returned account into each test function that names `account` as a parameter. The fixture uses the default function scope, so each test receives a freshly created account.

## Run

From the `Lab_04` directory:

```powershell
python -m pytest .\Fixtures -q
```

## Note

The example `BankAccount.withdraw` method checks that a withdrawal does not exceed the current balance, but it does not reject negative withdrawal amounts.
