#### Lab 02 Main Index (`Lab_02/README.md`)

```markdown
# Lab 02: Writing Effective Test Cases

| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |

---

## Modules

| Subfolder | Objective |
| :--- | :--- |
| **`aaa_pattern/`** | Rigorous separation of Arrange, Act, and Assert steps. |
| **`test_independence/`** | Avoiding shared mutable state across test functions. |
| **`boundary_value_analysis/`** | Testing upper, lower, and edge boundaries. |
| **`descriptive_naming/`** | Self-documenting function naming schemes. |
| **`positive_negative_testing/`** | Verifying system behavior under valid and invalid inputs. |

---

## Execution Commands

```bash
# Run all Lab 02 subfolders
pytest Lab_02/ -v

# Run boundary value tests
pytest Lab_02/boundary_value_analysis/ -v