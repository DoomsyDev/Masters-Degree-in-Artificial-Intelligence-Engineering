# Practice 02 — if / elif / else

score = float(input("Score (0-20): "))

if score < 0 or score > 20:
    print("Invalid score.")
elif score < 10:
    print("Fail")
elif score < 14:
    print("Pass")
elif score < 18:
    print("Good")
else:
    print("Excellent")
