# Practice 04 — Functions

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = float(input("First number: "))
b = float(input("Second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))

if b != 0:
    print("Division:", divide(a, b))
else:
    print("Cannot divide by zero.")
