# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

# Perform calculation using Match Case
match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
            result = None
    case _:
        print(f"Invalid operation: {operation}")
        result = None

# Output the result
if result is not None:
    print(f"The result is {result}.")
