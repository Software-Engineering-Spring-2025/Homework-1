# main.py

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y 

# function that calls other functions

def caller(op, num1, num2):
    if op == '+': return add(num1, num2)
    elif op == '-': return subtract(num1, num2)
    elif op == '*': return multiply(num1, num2)
    elif op == '/': return divide(num1, num2)
    else: print("operation does not match any existing function")
