# Checking a number for being odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# A simple calculator
def calculate(num1, operator, num2):
    """
    Performs basic arithmetic operations based on the provided operator.

    Args:
        num1: First operand (float).
        operator: Mathematical operator (string).
        num2: Second operand (float).

    Returns:
        The result of the calculation (float).
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Cant divide by zero"
        else:
            return num1 / num2
    else:
        return "Invalid operator"


while True:
    # Get user input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform calculation and handle errors
    result = calculate(num1, operator, num2)

    # Print the result
    print(result)

    # Ask if user wants to continue
    choice = input("Do you want to perform another calculation? (y/n): ")
    if choice.lower() != "y":
        break

print("Thank you for using the calculator!")


# Printing the Fibonacci
def fibonacci(n):
    """
    Prints the Fibonacci series up to the nth term.

    Args:
        n: Number of terms to print (integer).
    """
    # Initialize first two terms
    a, b = 0, 1

    # Print the first two terms if n is greater than or equal to 2
    if n >= 2:
        print(a, b, end=" ")

    # Iterate for n-2 times to print remaining terms
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c


# Get user input for number of terms
num_terms = int(input("Enter the number of terms: "))

# Print the Fibonacci series
fibonacci(num_terms)

print("\n")
