# 08 — Exception Handling

## Theory

Exceptions are errors that occur while a program is running.

```python
number = int(input("Number: "))
```

If the user enters text, a `ValueError` can occur.

## try / except

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid value")
```

## else

Runs when no exception occurs.

```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid value")
else:
    print(f"You entered {number}")
```

## finally

Runs whether or not an exception occurs.

```python
try:
    ...
except ValueError:
    ...
finally:
    print("Finished")
```

## Multiple exceptions

```python
try:
    result = 10 / number
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Best practices

Avoid using a bare `except:` unless there is a specific reason.

## Exercise

Create a calculator that keeps running when the user enters invalid values or tries to divide by zero.
