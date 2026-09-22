---

#### Lab 03 Main Index (`Lab_03/README.md`)

```markdown
# Lab 03: Assertions and Test Organization

| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

---

## Modules

| Subfolder | Objective |
| :--- | :--- |
| **`collections_floats/`** | Complex data structures and floating-point assertions using `pytest.approx`. |
| **`test_classes/`** | Test suite encapsulation inside classes (`Test*`). |
| **`using_markers/`** | Tagging and running tests by marker (`smoke`, `slow`, `regression`). |
| **`skipping_expected_failures/`** | Handling dynamic skips (`skip`, `skipif`) and open bugs (`xfail`). |
| **`configurewithpytest/`** | Declarative workspace configuration via `pytest.ini`. |

---

## Execution Commands

```bash
# Run all Lab 03 subfolders
pytest Lab_03/ -v

# Run smoke tests only
pytest Lab_03/ -m smoke -v