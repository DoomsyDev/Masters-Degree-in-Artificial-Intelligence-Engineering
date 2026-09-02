# Practice 06 — List Comprehensions

squares = [n ** 2 for n in range(1, 21)]
even_numbers = [n for n in range(1, 101) if n % 2 == 0]

names = ["Alice", "John", "Alexander", "Mary", "Fernando"]
long_names = [name for name in names if len(name) > 5]

print("Squares:", squares)
print("Even numbers:", even_numbers)
print("Names with more than 5 characters:", long_names)
