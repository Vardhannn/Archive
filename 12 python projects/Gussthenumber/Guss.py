import random

def Guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"guss any number between 1 to {x} "))
        if guess < random_number:
            print("sorry, too small try again")
        elif guess > random_number:
            print("sorry, too high try again")
    print(f"you guessed it correctly the number is {random_number}")

Guess(10)