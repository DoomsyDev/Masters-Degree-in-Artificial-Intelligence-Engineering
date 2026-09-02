# Practice 09 — File Reading and Writing

filename = "names.txt"

quantity = int(input("How many names do you want to save? "))

with open(filename, "w", encoding="utf-8") as file:
    for i in range(quantity):
        name = input(f"Name {i + 1}: ")
        file.write(name + "\n")

print("\nSaved names:")

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print("-", line.strip())
