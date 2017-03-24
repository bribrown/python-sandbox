# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

def main():
    rn = random.randint(1, 9)
    ug = 0
    attempts = 0

    while ug != rn and ug != 'exit':
        ug = int(input('Guess a number between 1 and 9: '))
        attempts += 1

        if ug == 'exit':
            exit()

        if ug > 9 or ug < 1:
            print('Your guess is not in the range of 1 - 9')
        elif ug == rn:
            print('You guessed the number.')
            print('It took ' + str(attempts) + ' guesses')
        elif ug < rn:
            print('Your guess is less than the number')
        else:
            print('Your guess is greater then the number')


if __name__ == "__main__": main()

