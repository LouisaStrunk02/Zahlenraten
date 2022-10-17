import random

num = random.randint(1, 20)
attempts = 0

print("Hallo, wie heißt du?")
name = input()

print("Hallo " + name + "! Ich denke an eine Zahl zwischen 1 und 20. Welche ist es?")

while True:

    guess = int(input())
    attempts += 1

    if guess < num:
        print("Dein Versuch ist zu niedrig. Rate erneut!")

    if guess > num:
        print("Dein Versuch ist zu hoch. Rate erneut!")

    if guess == num:
        print("Gut gemacht! Du hast die richtige Zahl nach nur " + str(attempts) + " Versuchen erraten")
        break
