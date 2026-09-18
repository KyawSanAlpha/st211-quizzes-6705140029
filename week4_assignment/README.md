# Week 4 Assignment

**Student ID:** `6705140029`  
**Student Name:** `Kyaw San`

## Overview

This assignment demonstrates core Python testing practices with `pytest`. It is organized into three exercise folders covering assertion techniques, organized unit tests, and positive/negative testing.

## Folder Contents

### `assertion_testing`

This folder demonstrates assertions for different data types and common comparison techniques.

- Uses `pytest.approx` for floating-point comparisons.
- Tests list equality and sorted list contents.
- Tests dictionary equality.
- Tests set intersection.

### `organized_testing`

This folder contains a simple `ShoppingCart` class and focused unit tests.

- Tests that a new cart starts empty.
- Tests that a new cart total is zero.
- Tests that adding an item increases the count.
- Tests that item prices are added correctly.

Each test focuses on one behavior of the shopping cart.

### `positive_negative_testing`

This folder tests input validation with both accepted and rejected values.

- Validates email addresses.
- Validates ages from `0` through `150`.
- Tests valid inputs in `test_positive.py`.
- Tests invalid inputs and expected `ValueError` or `TypeError` exceptions in `test_negative.py`.

## Requirements

- Python 3
- pytest

Install pytest if needed:

```powershell
python -m pip install pytest
```

## Run All Week 4 Tests

Open a terminal in the repository root and run:

```powershell
python -m pytest st211-quizzes-6705140029/week4_assignment
```

## Run Tests by Exercise

```powershell
python -m pytest st211-quizzes-6705140029/week4_assignment/assertion_testing
python -m pytest st211-quizzes-6705140029/week4_assignment/organized_testing
python -m pytest st211-quizzes-6705140029/week4_assignment/positive_negative_testing
```

## Test Focus

The assignment practices:

- Writing clear `assert` statements.
- Comparing floating-point values safely.
- Testing collections and their contents.
- Organizing tests by behavior.
- Testing both successful and failing inputs.
- Checking that functions raise the correct exception type.
