def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y


def calculator():
    """Interactive calculator"""
    print("=" * 40)
    print("        SIMPLE CALCULATOR")
    print("=" * 40)
    print("\nOperations:")
    print("  + : Addition")
    print("  - : Subtraction")
    print("  * : Multiplication")
    print("  / : Division")
    print("  q : Quit\n")
    
    while True:
        try:
            # Get first number
            num1 = float(input("Enter first number (or 'q' to quit): "))
            
            # Get operation
            operation = input("Enter operation (+, -, *, /): ").strip()
            
            if operation.lower() == 'q':
                print("Thank you for using the calculator!")
                break
            
            # Get second number
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            else:
                print("Invalid operation! Please use +, -, *, or /\n")
                continue
            
            # Display result
            print(f"\n{num1} {operation} {num2} = {result}\n")
            
        except ValueError:
            print("Invalid input! Please enter valid numbers.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")


if __name__ == "__main__":
    calculator()
