import random

MIN_NUMBER = 1
MAX_NUMBER = 100
new_game = True
distance_from_number = 0

print("Hallo, wie heißt du?")
name = input()

while new_game == True:

    number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print("Hallo " + name + "! Ich denke an eine Zahl zwischen " + str(MIN_NUMBER) + " und " + str(MAX_NUMBER) + ". Welche ist es?")

    while True:

        current_guess = input()

        if not current_guess.isnumeric():
            while not current_guess.isnumeric():
                print("Bitte gib nur Zahlen ein.")
                current_guess = input()
        
        guess = int(current_guess)

        while guess < MIN_NUMBER or guess > MAX_NUMBER:
            print("Gib bitte eine Zahl zwischen " + str(MIN_NUMBER) + " und " + str(MAX_NUMBER) + " an :)")
            break

        if guess < number_to_guess and guess >= MIN_NUMBER:

            if number_to_guess - guess <= 10 and attempts == 0:
                distance_from_number = number_to_guess - guess
                print("Heiß")
            elif number_to_guess - guess > 10 and attempts == 0:
                distance_from_number = number_to_guess - guess
                print("Kalt")
            
            if number_to_guess - guess < distance_from_number and attempts > 0:
                distance_from_number = number_to_guess - guess
                print("wärmer")
            elif number_to_guess - guess >= distance_from_number and attempts > 0:
                distance_from_number = number_to_guess - guess
                print("kälter")

            print("Dein Versuch ist zu niedrig. Rate erneut!")
            attempts += 1

        if guess > number_to_guess and guess <= MAX_NUMBER:

            if guess - number_to_guess <= 10 and attempts == 0:
                distance_from_number = guess - number_to_guess
                print("Heiß")
            elif guess - number_to_guess > 10 and attempts == 0:
                distance_from_number = guess - number_to_guess
                print("Kalt")

            if guess - number_to_guess < distance_from_number and attempts > 0:
                distance_from_number = guess - number_to_guess
                print("wärmer")
            elif guess - number_to_guess >= distance_from_number and attempts > 0:
                distance_from_number = guess - number_to_guess
                print("kälter")

            print("Dein Versuch ist zu hoch. Rate erneut!")
            attempts += 1

        if guess == number_to_guess:
            print("Gut gemacht! Du hast die richtige Zahl nach nur " + str(attempts) + " Versuchen erraten")
            print("Möchtest du noch einmal spielen? y/n")
            again = input()
            attempts += 1

            while True:
                if again == "y":
                    new_game = True
                    break
                elif again == "n":
                    new_game = False
                    break
                else:
                    print("Bitte gib y für ja und n für nein ein")

            break
