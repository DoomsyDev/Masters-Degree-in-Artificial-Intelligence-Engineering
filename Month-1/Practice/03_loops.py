# Practice 03 — for and while loops

number = int(input("Number for the multiplication table: "))

print("\nMultiplication table:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

print("\nEnter numbers. Type 0 to finish.")
total = 0

while True:
    value = int(input("Number: "))

    if value == 0:
        break

    total += value

print(f"Total: {total}")
