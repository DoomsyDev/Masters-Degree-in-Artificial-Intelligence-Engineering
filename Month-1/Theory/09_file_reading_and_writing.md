# 09 — File Reading and Writing

## Theory

Python can work with files using `open()`.

## Reading

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Using `with` ensures that the file is properly closed.

## Writing

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python!")
```

`w` replaces existing content.

## Appending

```python
with open("data.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line")
```

## Reading line by line

```python
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
```

## Common modes

- `r` — read
- `w` — write/replace
- `a` — append
- `x` — create a new file

## Exercise

Create a program that saves names to a file and then reads and displays them.
