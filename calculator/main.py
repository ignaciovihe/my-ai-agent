# calculator/main.py

import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main():
    # Initialize the Calculator object
    calculator = Calculator()

    # Check if an expression is provided as a command-line argument
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    # Join command-line arguments to form the expression
    expression = " ".join(sys.argv[1:])

    try:
        # Evaluate the expression using the calculator
        result = calculator.evaluate(expression)

        # If the result is not None, format and print the output
        if result is not None:
            to_print = format_json_output(expression, result)
            print(to_print)
        else:
            # Handle cases where the expression is empty or whitespace only
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        # Catch and print any errors during evaluation
        print(f"Error: {e}")


if __name__ == "__main__":
    main()