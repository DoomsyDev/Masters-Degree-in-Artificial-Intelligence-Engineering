# Practice 08 — Exception Handling

while True:
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
        result = a / b
    except ValueError:
        print("Error: enter valid numbers.")
    except ZeroDivisionError:
        print("Error: cannot divide by zero.")
    else:
        print(f"Result: {result}")
        break
