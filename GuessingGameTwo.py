# In a previous exercise, [GuessingGameOne] we’ve written a program that “knows” a number and asks a user to guess it.
#
# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
#
# At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# As the writer of this program, you will have to choose how your program will strategically guess. A naive
# strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range),
# and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!

import random

def main():
    guess = random.randint(0, 100)
    number_of_guesses = 1

    print('My guess: ' + str(guess))

    response = input('Did I guess your number? (higher, lower, or yes): ')

    if response == 'yes':
        print('Yay for me!')
        exit()

    while response != 'yes':
        if response == 'higher':
            gl = range(guess+1,101)
            for next_guess in gl:
                print('My guess: ' + str(next_guess))
                response = input('Did I guess your number? (higher, lower, or yes): ')
                if response == 'yes':
                    number_of_guesses += 1
                    print('Yay for me!')
                    print('Number of guesses: ' + str(number_of_guesses))
                    exit()
                else:
                    next_guess += 1
                    number_of_guesses += 1
        elif response == 'lower':
            gl = range(guess-1,0,-1)
            for next_guess in gl:
                print('My guess: ' + str(next_guess))
                response = input('Did I guess your number? (higher, lower, or yes): ')
                if response == 'yes':
                    number_of_guesses += 1
                    print('Yay for me!')
                    print('Number of guesses: ' + str(number_of_guesses))
                    exit()
                else:
                    next_guess -= 1
                    number_of_guesses += 1
        else:
            print('Invalid input')
            response = input('Did I guess your number? (higher, lower, or yes): ')


if __name__ == "__main__": main()

# import random
# 
# MINIMUM = 0
# MAXIMUM = 100
# NUMBER = random.randint(MINIMUM, MAXIMUM)
# TRY = 0
# RUNNING = True
# ANSWER = None
#
# while RUNNING:
#     print
#     "Is it %s?" % str(NUMBER)
#     ANSWER = raw_input()
#     if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
#         NUMBER -= random.randint(1, 4)
#     elif "no" in ANSWER.lower() and "higher" in ANSWER.lower():
#         NUMBER += random.randint(1, 4)
#     elif ANSWER.lower() == "no":
#         print
#         "Higher or lower?"
#         ANSWER = raw_input()
#         if ANSWER.lower() == "higher":
#             NUMBER += random.randint(1, 4)
#         elif ANSWER.lower() == "lower":
#             NUMBER -= random.randint(1, 4)
#     elif ANSWER.lower() == "yes":
#         if TRY < 2:
#             print
#             "Yes! It only took me %s try!" % str(TRY)
#         elif TRY < 2 and TRY < 10:
#             print
#             "Pretty well for a robot, %s tries." % str(TRY)
#         else:
#             print
#             "That's so bad, %s tries." % str(TRY)
#         RUNNING = False
#     TRY += 1
#
# print
# "Thanks for the game!"