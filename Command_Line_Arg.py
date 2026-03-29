import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

x = int(sys.argv[1])
operation = sys.argv[2]
y = int(sys.argv[3])

if operation == "add":
    result = add (x,y)
    print(f"Result of addition: {result}")
elif operation == "sub":
    result = subtract(x,y)
    print(f"Result of subtraction: {result}") 
elif operation == "mul":
    result = multiply(x,y)
    print(f"Result of multiplication: {result}")
elif operation == "div":
    result = divide(x,y)
    print(f"Result of division: {result}")
else:
    print("Invalid operation")