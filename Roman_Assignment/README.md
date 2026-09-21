# Roman Assignment

**Student ID:** `6705140029`  
**Student Name:** `Kyaw San`

## Project Overview
A robust Python command-line utility and module for converting Roman numerals into integers with strict syntax validation and unit test coverage.

## Features
Bidirectional Validation: Rejects invalid or non-canonical Roman numerals (e.g., "IIII" or "VX") by cross-checking conversions.
Input Sanitization: Automatically trims whitespace and handles case sensitivity (e.g., " xix " $\rightarrow$ 19).
Interactive CLI: Built-in command-line interface menu for interactive conversions.
Error Handling: Clear exception raising (ValueError, TypeError) for invalid inputs or incorrect types.
Comprehensive Test Suite: Includes automated unit tests covering valid conversions, edge cases, and invalid inputs using pytest.

## How It Works
Conversion Algorithm
Sanitization & Checking: Trims whitespace and converts characters to uppercase.
Subtractive Rule Parsing: Iterates through characters from left to right. If a character's value is smaller than the following character's value, it is subtracted from the total; otherwise, it is added.
Canonical Verification: Re-converts the calculated integer back into a Roman numeral using to_roman(). If the result does not match the input string exactly, a ValueError is raised (e.g., "IIII" yields 4, but to_roman(4) yields "IV", triggering a validation failure).
