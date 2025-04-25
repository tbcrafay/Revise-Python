''' Generate a random number within a certain range.
Prompt the user to guess the number.
Use a while loop to continue the game until the user guesses correctly.
Provide feedback to the user (e.g., "Too high!", "Too low!"). '''

import random

def number_guessing_game():

    first_num = 1
    ranged_num = 100
    secret_num = random.randint(first_num, ranged_num)
    guess = None
    attempts = 0

    while guess != secret_num:

        guess_in = input("Take the guess: ")
        guess = int(guess_in)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.") 

if __name__ == "__main__":
    number_guessing_game()
