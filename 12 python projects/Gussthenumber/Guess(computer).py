
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(low , high)
        feedback = input(f"Is guess {guess} too high or too low ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"computer guess the number correctly the number is {guess}")

computer_guess(5)