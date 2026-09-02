# 03 — for and while loops

## Theory

Loops allow code to be repeated.

## for

Use `for` when you want to iterate over a sequence or a known range.

```python
for number in range(5):
    print(number)
```

Output:

```text
0
1
2
3
4
```

### range

```python
range(5)
range(2, 6)
range(0, 10, 2)
```

## while

A `while` loop repeats while a condition is true.

```python
counter = 0

while counter < 5:
    print(counter)
    counter += 1
```

Make sure the condition can eventually become false.

## break

Stops the loop.

```python
while True:
    answer = input("Type quit: ")
    if answer == "quit":
        break
```

## continue

Skips to the next iteration.

```python
for number in range(10):
    if number % 2 == 0:
        continue
    print(number)
```

## Exercise

Create one program that prints the multiplication table of a number using `for`, and another that keeps asking for numbers until the user enters `0` using `while`.
