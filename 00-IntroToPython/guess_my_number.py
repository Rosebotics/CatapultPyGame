import random

print("Guess My Number")
secret_number = random.randint(1, 100)
counter = 0

while True:
    guess = int(input("Guess the secret number (between 1 and 100): "))
    counter += 1
    if guess > secret_number:
        print(f"{guess} is too high. Guess lower!")
    elif guess < secret_number:
        print(f"{guess} is too low. Guess higher!")
    else:
        print("You win!")
        break

print(f"It took you {counter} guesses.")
