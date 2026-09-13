# Python Salary Increment Calculator

A simple Python program that calculates an employee's salary increment based on their years of service.

## Features

- Takes current salary as user input
- Takes years of service as user input
- Calculates the increment percentage based on service years
- Displays the current salary
- Displays the increment amount
- Displays the new salary
- Handles different service-year conditions

## Increment Rules

| Service Years | Increment |
|--------------|-----------|
| 0            | Junior    |
| 1            | 2%        |
| 2            | 4%        |
| 3            | 6%        |
| 4            | 8%        |
| 5–7          | 10%       |
| 8+           | Senior    |

## Concepts Used

- `input()`
- `int()`
- `if / elif / else`
- Comparison operators
- Arithmetic operators
- Percentage calculation
- f-strings

## Example

```text
Enter Current Salary : 50000
Enter Service years : 5

Your Current Salary 50000
Incrasing Salary 5000.0
After Increment your New Salary is 55000.0
