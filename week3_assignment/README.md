# Week 3 Assignment

**Student ID:** `6705140029`  
**Student Name:** `Kyaw San`

This folder contains Python examples and pytest tests for unit testing, boundary testing, independent tests, and dependent tests.

## Files

- `bank.py`
  - Defines the `BankAccount` class.
  - `deposit(amount)` adds money to the balance. Zero is allowed, but negative deposits raise `ValueError`.
  - `withdraw(amount)` subtracts money from the balance. Withdrawing more than the balance raises `ValueError`.
  - Includes a small demonstration that deposits and withdraws money when the file is run directly.
- `grades.py`
  - Defines `letter_grade(score)`.
  - Valid scores must be between `0` and `100`.
  - Returns `A` for scores from 80 to 100, `B` for 70 to 79, `C` for 60 to 69, and `F` for scores below 60.
  - Scores outside the valid range raise `ValueError`.
- `test_bank.py`
  - Tests deposits, withdrawals, zero deposits, and a combined account workflow.
- `test_grades.py`
  - Tests grade boundaries, valid limits, and invalid scores.
- `test_independent.py`
  - Tests each account operation with a new account for every test.
- `test_dependent.py`
  - Demonstrates tests that share one account and therefore depend on execution state.
- `test_name.py`
  - Tests expected errors for negative deposits, excessive withdrawals, and withdrawing the exact balance.

## Requirements

- Python 3
- pytest

Install pytest if needed:

```powershell
python -m pip install pytest
```

## Run the Tests

Open a terminal in this folder and run all tests:

```powershell
python -m pytest
```

Run an individual test file:

```powershell
python -m pytest test_bank.py
python -m pytest test_grades.py
python -m pytest test_independent.py
python -m pytest test_dependent.py
python -m pytest test_name.py
```

Run a test from the repository root instead:

```powershell
python -m pytest st211-quizzes-6705140029/week3_assignment/test_bank.py
```

## Run the Example

From this folder, run:

```powershell
python bank.py
```

The example creates an account with a balance of `100`, deposits `100`, and then withdraws `50`.
