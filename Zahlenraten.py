import random

num = random.randint(1, 20)

print("Hallo Spieler! Ich denke an eine Zahl zwischen 1 und 20. Welche ist es?")

while True:

    guess = int(input())

    if guess < num:
        print("Dein Versuch ist zu niedrig. Rate erneut!")

    if guess > num:
        print("Dein Versuch ist zu hoch. Rate erneut!")

    if guess == num:
        print("Gut gemacht! Du hast die richtige Zahl erraten")
        break
