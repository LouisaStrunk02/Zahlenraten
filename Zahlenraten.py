import random

game = True
guess = 0

print("Hallo, wie heißt du?")
name = input()

while game == True:

    num = random.randint(1, 100)
    attempts = 0

    print("Hallo " + name + "! Ich denke an eine Zahl zwischen 1 und 100. Welche ist es?")

    while True:

        tempNumber = input()

        if not tempNumber.isnumeric():
            while not tempNumber.isnumeric():
                print("Bitte gib nur Zahlen ein.")
                tempNumber = input()
        
        guess = int(tempNumber)

        while guess < 1 or guess > 100:
            print("Gib bitte eine Zahl zwischen 1 und 100 an :)")
            break

        if guess < num and guess >= 1:

            if num - guess <= 10:
                print("Heiß")
            else :
                print("Kalt")

            print("Dein Versuch ist zu niedrig. Rate erneut!")
            attempts += 1

        if guess > num and guess <= 100:

            if guess - num <= 10:
                print("Heiß")
            else :
                print("Kalt")

            print("Dein Versuch ist zu hoch. Rate erneut!")
            attempts += 1

        if guess == num:
            print("Gut gemacht! Du hast die richtige Zahl nach nur " + str(attempts) + " Versuchen erraten")
            print("Möchtest du noch einmal spielen? y/n")
            again = input()
            attempts += 1

            while True:
                if again == "y":
                    game = True
                    break
                elif again == "n":
                    game = False
                    break
                else:
                    print("Bitte gib y für ja und n für nein ein")

            break
