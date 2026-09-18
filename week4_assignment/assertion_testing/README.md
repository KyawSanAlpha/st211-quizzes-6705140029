# Assertion Testing

**Student ID:** `6705140029`  
**Student Name:** `Kyaw San` 

This folder contains pytest examples showing how to write assertions for floating-point values and collections.

## Files

- `test_floats.py`
  - Uses `pytest.approx` to compare floating-point results safely.
  - Demonstrates that `0.1 + 0.2` should be compared approximately with `0.3` because floating-point arithmetic can introduce small precision differences.
  - Demonstrates an inequality assertion without `approx`.
- `test_collections.py`
  - Tests list equality.
  - Tests list contents after sorting.
  - Tests dictionary equality. Dictionary key order does not affect equality.
  - Tests set intersection.

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

Run an individual file:

```powershell
python -m pytest test_floats.py
python -m pytest test_collections.py
```

From the repository root, run:

```powershell
python -m pytest st211-quizzes-6705140029/week4_assignment/assertion_testing
```

## Notes

- Use `pytest.approx` when comparing calculated floating-point values.
- Python collection assertions compare values and structure. Dictionary key order does not matter.
- In `test_collections.py`, `test_set_operations` is currently indented inside `test_dict_equality`, so it is not collected as a separate top-level test by pytest.
