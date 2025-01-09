def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error! Division by zero."

# User input
print("Select operation: +, -, *, /")
operation = input("Enter operation: ")

num1 = float(input("Enter first number: "))
num2 = input("Enter second number: ")  # Error here: num2 is a string, not a float.

# Perform operation and display result
if operation == '+': print(f"Result: {add(num1, num2)}")
elif operation == '-': print(f"Result: {subtract(num1, num2)}")
elif operation == '*': print(f"Result: {multiply(num1, num2)}")
elif operation == '/': print(f"Result: {divide(num1, num2)}")
else: print(f"Invalid operation: {operation}")


## I need a syntax error for the hover feature to work
print(hello world
