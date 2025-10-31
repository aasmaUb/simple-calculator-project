# calculator.py
# Created by Aasma Ubaid
# Description: Advanced calculator with loop, error handling, and exit option

import operations


def run_calculator():
    """Run an interactive calculator that reuses functions from operations.py."""
    print("Welcome to Aasma's Calculator!")
    print("Type 'q' at any number prompt to quit.\n")

    while True:
        # Get first number
        raw = input("Enter the first number (or 'q' to quit): ").strip()
        if raw.lower() == 'q':
            break
        try:
            num1 = float(raw)
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.\n")
            continue

        # Get second number
        raw = input("Enter the second number (or 'q' to quit): ").strip()
        if raw.lower() == 'q':
            break
        try:
            num2 = float(raw)
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.\n")
            continue

        # Operator selection
        print("Choose an operator: +, -, *, /")
        operator = input("Enter operator: ").strip()

        # Call appropriate function from operations.py
        if operator == '+':
            result = operations.add(num1, num2)
        elif operator == '-':
            result = operations.subtract(num1, num2)
        elif operator == '*':
            result = operations.multiply(num1, num2)
        elif operator == '/':
            result = operations.divide(num1, num2)
        else:
            print("❌ Invalid operator. Please choose +, -, *, or /.\n")
            continue

        # Show result (operations.divide returns an error message string if division by zero)
        if result is not None:
            print(f"✅ {num1} {operator} {num2} = {result}\n")

        # Ask whether to continue
        choice = input("Perform another calculation? (yes/no): ").strip().lower()
        if choice in ('yes', 'y'):
            continue
        else:
            print("👋 Thank you for using Aasma's Calculator! Goodbye.")
            break


if __name__ == "__main__":
    run_calculator()
