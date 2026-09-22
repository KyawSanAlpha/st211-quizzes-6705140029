### Folder-Specific `README.md` Files

#### Lab 01 Main Index (`Lab_01/README.md`)

```markdown
# Lab 01: Testing Fundamentals and Your First Automated Test

| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

---

## Modules

| Subfolder | Objective |
| :--- | :--- |
| **`setup_environment/`** | Basic pytest assertions and project environment validation. |
| **`calculator_module/`** | Unit testing a calculator class utilizing the AAA layout. |
| **`failing_and_exceptions/`** | Reading failure logs and testing code exceptions using `pytest.raises`. |

---

## Execution Commands

```bash
# Run all Lab 01 subfolders
pytest Lab_01/ -v

# Run module individually
pytest Lab_01/calculator_module/ -v
