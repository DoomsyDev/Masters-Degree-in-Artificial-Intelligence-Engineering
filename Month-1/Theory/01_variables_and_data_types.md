# 01 — Variables and Data Types

## Theory

A variable is a name associated with a value.

```python
name = "Alice"
age = 20
height = 1.70
student = True
```

Python determines the type of a value automatically.

## Main data types

- `int` — integers
- `float` — decimal numbers
- `str` — text
- `bool` — `True` or `False`
- `None` — absence of a value

```python
age = 25
price = 19.99
name = "John"
active = True
result = None
```

## Checking a type

```python
print(type(age))
```

## Type conversion

```python
age = int("25")
price = float("19.99")
text = str(100)
```

## Basic operators

```python
addition = 10 + 5
subtraction = 10 - 5
multiplication = 10 * 5
division = 10 / 5
power = 2 ** 3
remainder = 10 % 3
```

## User input

`input()` always returns a string.

```python
name = input("Name: ")
age = int(input("Age: "))
```

## Best practices

- Use descriptive names such as `age`, `total_price`, and `username`.
- Avoid meaningless names when the purpose is unclear.
- Use `snake_case` for variables and functions.

## Exercise

Create a program that asks for a person's name, age, and height, then prints the values and their types.
