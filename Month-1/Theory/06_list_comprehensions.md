# 06 — List Comprehensions

## Theory

List comprehensions provide a concise way to create lists.

Traditional approach:

```python
squares = []

for number in range(10):
    squares.append(number ** 2)
```

Using a comprehension:

```python
squares = [number ** 2 for number in range(10)]
```

## With a condition

```python
even_numbers = [number for number in range(20) if number % 2 == 0]
```

## General structure

```python
[expression for item in iterable if condition]
```

The condition is optional.

## Examples

```python
names = ["alice", "john", "mary"]
uppercase = [name.upper() for name in names]
```

## Best practice

Do not make comprehensions unnecessarily complicated. Readability is more important than saving lines.

## Exercise

Create lists containing:
1. The squares from 1 to 20.
2. The even numbers from 1 to 100.
3. Names with more than 5 characters.
