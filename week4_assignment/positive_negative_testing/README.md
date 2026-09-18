# Positive and Negative Testing

**Student ID:** `6705140029`  
**Student Name:** `Kyaw San`

This folder contains validation functions and pytest tests for both valid (positive) and invalid (negative) inputs.

## Files

- `validators.py`
  - Defines `validate_email(email)`.
  - Returns `True` for an email with a valid format.
  - Raises `ValueError` for an invalid email format.
  - Defines `validate_age(age)`.
  - Returns `True` for integer ages from `0` through `150`.
  - Raises `TypeError` when the age is not an integer.
  - Raises `ValueError` when the age is outside the range `0` to `150`.
- `test_positive.py`
  - Tests valid email addresses.
  - Tests a valid age.
  - Tests the minimum and maximum accepted ages.
- `test_negative.py`
  - Tests email addresses without a valid at-sign or domain.
  - Tests a negative age.
  - Tests a string age and expects `TypeError`.

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

Run the test files individually:

```powershell
python -m pytest test_positive.py
python -m pytest test_negative.py
```

From the repository root, run:

```powershell
python -m pytest st211-quizzes-6705140029/week4_assignment/positive_negative_testing
```

## Expected Result

The test suite should complete with eight passing tests:

```text
8 passed
```
