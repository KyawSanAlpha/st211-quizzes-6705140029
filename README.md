# 192-211 Automated Software Testing - Comprehensive Lab Portfolio

| Attribute | Details |
| :--- | :--- |
| **Course** | 192-211 Automated Software Testing |
| **Institution** | International College, Siam University |
| **Student Name** | Kyaw San |
| **Student ID** | 6705140029 |
| **Framework** | Python 3.8+ / `pytest` |

---

## Repository Overview

This repository contains structured coursework and automated test suites for **192-211 Automated Software Testing**. Each lab is organized into domain-specific topic folders representing discrete software testing concepts and lab steps.

```text
.
├── Lab_01/                     # Testing Fundamentals & Initial Automation
│   ├── setup_environment/      # First assertions and test execution
│   ├── calculator_module/      # Core functions and basic unit testing
│   └── failing_and_exceptions/ # Error handling and expected exception testing
├── Lab_02/                     # Writing Effective Test Cases
│   ├── aaa_pattern/            # Arrange-Act-Assert design pattern
│   ├── test_independence/      # State isolation and order-independent runs
│   ├── boundary_value_analysis/# Testing edge cases and boundary thresholds
│   ├── descriptive_naming/     # Self-documenting test specifications
│   └── positive_negative_testing/ # Valid input vs. invalid input validation
└── Lab_03/                     # Assertions & Test Suite Organization
    ├── collections_floats/     # Collections assertions & approx float testing
    ├── test_classes/           # Grouping suites within class wrappers
    ├── using_markers/          # Custom tag filtering (smoke, slow, regression)
    ├── skipping_expected_failures/ # Conditional skips and xfail tags
    └── configurewithpytest/    # Project-wide setup using pytest.ini
└── Roman_Assignment/           # Roman numeral conversion and validation
    ├── roman.py                # Roman numeral converter entry point
    └── test_roman.py           # Converter behavior and invalid-input tests

    Lab Modules Summary
Lab 01: Testing Fundamentals

    setup_environment/: Initial environment setup and baseline test execution using pytest.

    calculator_module/: Testing unit operations (add, subtract, multiply, divide).

    failing_and_exceptions/: Handling assertion failures, debugging output, and validating exceptions using pytest.raises.

Lab 02: Writing Effective Test Cases

    aaa_pattern/: Enforcing the Arrange-Act-Assert testing pattern for clear intent.

    test_independence/: Isolating test execution data to prevent shared state side-effects.

    boundary_value_analysis/: Evaluating critical min, max, and threshold scores.

    descriptive_naming/: Applying test_[what]_[condition]_[expected] conventions.

    positive_negative_testing/: Balancing happy-path and edge-case error assertions.

Lab 03: Assertions and Test Organization

    collections_floats/: Deep comparison on lists, sets, dicts, and float precision checks via pytest.approx.

    test_classes/: Encapsulating related test cases inside reusable test classes (Test*).

    using_markers/: Filtering test suites dynamically with custom markers (smoke, slow, regression).

    skipping_expected_failures/: Handling feature flags, skipped runs, and tracking known bugs with xfail.

    configurewithpytest/: Standardizing runtime configurations using pytest.ini and --strict-markers.

Roman Numeral Assignment

    Roman_Assignment/: Implementing Roman numeral conversion, including subtractive notation and validation of invalid inputs.

Execution Guide
Environment Setup
Bash

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install pytest

Running Test Suites
Bash

# Run all tests across the entire repository
pytest

# Run tests within a specific lab
pytest Lab_01/
pytest Lab_02/
pytest Lab_03/
pytest Roman_Assignment/

# Run a specific subfolder module
pytest Lab_03/collections_floats/ -v

# Run the Roman numeral assignment tests
pytest Roman_Assignment/test_roman.py -v