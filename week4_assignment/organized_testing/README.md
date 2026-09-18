# Organized Testing

**Student ID:** `6705140029`  
**Student Name:** `Kyaw San`

This folder contains a simple shopping-cart example and organized pytest tests. Each test checks one behavior of the `ShoppingCart` class.

## Files

- `shopping.py`
  - Defines the `ShoppingCart` class.
  - `add(name, price)` adds an item with its name and price.
  - `total()` returns the sum of all item prices.
  - `count()` returns the number of items in the cart.
- `test_shopping.py`
  - Tests that a new cart is empty.
  - Tests that a new cart has a total of zero.
  - Tests that adding an item increases the item count.
  - Tests that the total adds all item prices correctly.

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

Run the test file directly:

```powershell
python -m pytest test_shopping.py
```

From the repository root, run:

```powershell
python -m pytest st211-quizzes-6705140029/week4_assignment/organized_testing
```

## Expected Result

The test suite should complete with four passing tests:

```text
4 passed
```
