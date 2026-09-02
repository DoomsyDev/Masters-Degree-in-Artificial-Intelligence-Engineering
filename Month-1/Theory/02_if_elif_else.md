# 02 — if / elif / else

## Theory

Conditional statements allow a program to make decisions.

```python
if age >= 18:
    print("Adult")
```

## if and else

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## elif

Use `elif` to test additional conditions.

```python
if score < 10:
    print("Fail")
elif score < 14:
    print("Pass")
elif score < 18:
    print("Good")
else:
    print("Excellent")
```

Python checks conditions from top to bottom.

## Comparison operators

- `==` equal
- `!=` not equal
- `>` greater than
- `<` less than
- `>=` greater than or equal to
- `<=` less than or equal to

## Logical operators

### and

All conditions must be true.

```python
if age >= 18 and has_ticket:
    print("Entry allowed")
```

### or

At least one condition must be true.

```python
if day == "Saturday" or day == "Sunday":
    print("Weekend")
```

### not

Inverts a boolean value.

```python
if not raining:
    print("You can go outside")
```

## Exercise

Create a program that asks for a score from 0 to 20 and prints its classification.
