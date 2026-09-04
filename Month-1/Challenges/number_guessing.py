import random
import os

#initializing exercise
input_number_random = random.randrange(0, 100)
def input_by_user():
    return int(input("Adivinha o número de 0 a 100: "))

#verifications
while True:
    input_number = input_by_user()

    if 0 <= input_number <= 100:
        if input_number < input_number_random:
            print("É maior, tenta de novo")
        elif input_number > input_number_random:
            print("É menor, tenta de novo")    
        else:
            break
    else:
        print("O número tem de estar entre 0 e 100.")

print("Acertaste no número número:", input_number)