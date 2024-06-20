import random

print("Guess My Word")

def update_display_word(newest_guess, d, s):
    result = ""
    for k in range(len(d)):
        if newest_guess == s[k]:
            result += newest_guess
        else:
            result += d[k]
    return result


words = ["catapult", "funishment", "rose", "hulman", "fisher", "winston", "dave"]

secret_word = random.choice(words)
display_word = "*" * len(secret_word)
guessed_letters = []
print(display_word)
while True:
    print()
    guess = input("Guess a letter ")
    if guess in guessed_letters:
        print("You already guessed that")
        continue
    guessed_letters.append(guess)
    display_word = update_display_word(guess, display_word, secret_word)
    print(f"Word so far: {display_word}")
    print(f"Guesses so far: {guessed_letters}")
    if display_word == secret_word:
        break


print(f"Congrats, you got {secret_word} in {len(guessed_letters)} guesses.")
