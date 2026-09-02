# 07 — Classes and Objects

## Theory

A class defines the structure and behavior of objects.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Create an object:

```python
person = Person("Alice", 25)
```

## Attributes

```python
print(person.name)
print(person.age)
```

## Methods

Methods are functions defined inside a class.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, I am {self.name}")
```

## self

`self` refers to the current object instance.

## Inheritance

A class can inherit from another class.

```python
class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

## Exercise

Create a `BankAccount` class with a balance and methods called `deposit`, `withdraw`, and `show_balance`.
