| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

# Factory Fixtures

## Purpose

This folder demonstrates fixture factories: fixtures that provide a callable helper so a test can create one or more objects with different input data.

## Files

| File | Description |
| :--- | :--- |
| [bank.py](./bank.py) | Defines the `BankAccount` example class with deposit and withdrawal operations. |
| [test_factory.py](./test_factory.py) | Defines the `make_account` fixture and uses it to create accounts with different starting balances. |
| [test_factory_advanced.py](./test_factory_advanced.py) | Defines a `make_user` fixture factory and demonstrates its default and customized role values, plus fixture teardown. |

## Key concept

`make_account` returns a nested function that creates a `BankAccount` for a balance selected by the test. Similarly, `make_user` returns a factory function; it records the users created during a test and reports the count after the test finishes.

## Run

From the `Lab_04` directory:

```powershell
python -m pytest .\Factory_Fixtures -q
```

## Note

`test_multiple_accounts` currently creates two accounts but does not assert their balances or otherwise verify them. The example `BankAccount.withdraw` method also accepts a negative amount, which increases the balance.
