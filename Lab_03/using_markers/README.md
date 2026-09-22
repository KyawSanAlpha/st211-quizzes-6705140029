##### 3. `Lab_03/using_markers/README.md`
```markdown
# Custom Test Markers

**Student Name:** Kyaw San  
**Student ID:** 6705140029

## Folder Contents
- `pytest.ini`: Local marker registration file.
- `test_markers.py`: Suite containing `@pytest.mark.smoke`, `@pytest.mark.slow`, and `@pytest.mark.regression`.

## How to Test and Run
```bash
cd Lab_03/using_markers
pytest -m smoke -v
pytest -m "not slow" -v