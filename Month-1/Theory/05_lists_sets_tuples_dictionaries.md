# 05 — Lists, Sets, Tuples, and Dictionaries

## Lists

Ordered and mutable collections.

```python
fruits = ["apple", "banana", "orange"]
fruits.append("pear")
print(fruits[0])
```

## Tuples

Ordered and immutable collections.

```python
coordinates = (10, 20)
x, y = coordinates
```

## Sets

Collections that contain unique values.

```python
numbers = {1, 2, 2, 3}
print(numbers)
```

## Dictionaries

Store key-value pairs.

```python
person = {
    "name": "Alice",
    "age": 25
}

print(person["name"])
person["age"] = 26
```

## When should you use each?

- List: an ordered collection that may change.
- Tuple: an ordered collection that should not change.
- Set: a collection of unique values.
- Dictionary: data associated with keys.

## Exercise

Create a list of products, a set of categories, a tuple containing coordinates, and a dictionary containing information about a person.
