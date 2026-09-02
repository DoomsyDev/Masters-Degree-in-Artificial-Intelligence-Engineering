# 04 — Functions

## Theory

A function groups reusable code.

```python
def greet(name):
    print(f"Hello, {name}!")
```

Call it with:

```python
greet("Alice")
```

## Parameters

```python
def add(a, b):
    return a + b
```

## return

`return` sends a value back to the caller.

```python
result = add(10, 5)
print(result)
```

## Default arguments

```python
def greet(name="user"):
    print(f"Hello, {name}!")
```

## Keyword arguments

```python
def introduce(name, age):
    print(name, age)

introduce(age=20, name="Alice")
```

## Scope

Variables created inside a function are normally local to that function.

```python
def example():
    message = "Hello"
    print(message)
```

## Best practices

A function should have a clear purpose and a descriptive name.

## Exercise

Create functions for adding, subtracting, multiplying, and dividing two numbers.
