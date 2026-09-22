##### 5. `Lab_02/positive_negative_testing/README.md`
```markdown
# Positive and Negative Test Coverage

**Student Name:** Kyaw San  
**Student ID:** 6705140029

## Folder Contents
- `validators.py`: Logic for `validate_email` and `validate_age`.
- `test_positive.py`: Happy path tests for valid inputs.
- `test_negative.py`: Verification that invalid inputs raise correct exceptions.

## How to Test and Run
```bash
cd Lab_02/positive_negative_testing
pytest test_positive.py test_negative.py -v