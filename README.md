# 192-211 Automated Software Testing

| Info | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Institution** | International College, Siam University |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |
| **Testing Framework** | Python and `pytest` |

## Repository overview

This repository contains course labs, a mocking exercise, and a Roman numeral assignment. Each lab is divided into topic folders with example code and pytest tests.

```text
.
├── Lab_01/                  # Testing fundamentals and first automated tests
├── Lab_02/                  # Test design, independence, and input validation
├── Lab_03/                  # Assertions, markers, skips, and pytest configuration
├── Lab_04/                  # Fixtures, fixture scopes, and setup/teardown
├── Lab_05/                  # Parameterized tests and data-driven testing
├── Mock_Lab/                # Mocking a random temperature dependency
├── Roman_Assignment/        # Roman numeral conversion and validation
├── pytest.ini               # Repository-wide pytest settings and markers
└── README.md
```

## Lab topics

### Lab 01 - Testing fundamentals

- `setup_environment/`: initial pytest setup and a basic test.
- `calculator_module/`: calculator functions and unit tests.
- `failing_and_exceptions/`: assertion failures and expected exceptions.

### Lab 02 - Effective test cases

- `aaa_pattern/`: Arrange-Act-Assert structure.
- `boundary_value_analysis/`: tests around score thresholds.
- `descriptive_naming/`: descriptive test names.
- `positive_negative_testing/`: valid and invalid input cases.
- `test_independence/`: independent tests and state handling.

### Lab 03 - Assertions and test organization

- `collections_floats/`: collection assertions and approximate float comparisons.
- `configure_with_pytest/`: pytest configuration and strict marker behavior.
- `skipping_expected_failures/`: conditional skips and expected failures.
- `test_classes/`: grouping tests in classes.
- `using_markers/`: categorizing and selecting tests with markers.

### Lab 04 - Fixtures

- `Factory_Fixtures/`: fixture factories that create test data on demand.
- `Fixtures/`: basic reusable fixtures.
- `Fixtures_Shares/`: fixtures shared between test modules with `conftest.py`.
- `Scopes/`: function, module, and session fixture scopes.
- `SetUp&Teardown/`: resource setup and cleanup using yield fixtures.

### Lab 05 - Parameterized testing

- `DataDriven_Tesing/`: test cases loaded from CSV and JSON.
- `Ids&Readibility/`: generated and custom parameter IDs and parameter marks.
- `Parameterized_Fixtures/`: fixtures that run tests with multiple values.
- `Parameters/`: parametrized calculations, error cases, and combinations.
- `Parametrization/`: parametrized tests for math utilities.

### Other coursework

- `Mock_Lab/`: tests weather descriptions using a mocked temperature source; see the [Mock_Lab README](./Mock_Lab/README.md).
- `Roman_Assignment/`: Roman numeral conversion and input validation.

## Requirements and setup

- Python 3.8 or newer
- `pytest`

Create and activate a virtual environment, then install pytest:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install pytest
```

## Running tests

Run all tests discovered by the repository configuration:

```powershell
python -m pytest
```

Run a particular lab or exercise:

```powershell
python -m pytest Lab_01
python -m pytest Lab_02
python -m pytest Lab_03
python -m pytest Lab_04
python -m pytest Lab_05
python -m pytest Mock_Lab
python -m pytest Roman_Assignment
```

For folder names containing `&`, quote the path in PowerShell:

```powershell
python -m pytest '.\Lab_04\SetUp&Teardown'
python -m pytest '.\Lab_05\Ids&Readibility'
```

The root [pytest.ini](./pytest.ini) enables verbose output, short tracebacks, and strict marker validation. It also declares the `smoke`, `slow`, and `regression` markers.

## Current notes

Some exercises intentionally demonstrate incomplete or problematic tests. For example, the Lab 05 JSON uppercase example contains a numeric input although the test calls `.upper()`, and the `Ids&Readibility` discount test imports a module not present in that folder. Review individual lab READMEs and test output when running those exercises.
