# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number,
# the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

def main():
    target = list(random.sample(range(1, 10), 4))
    str_target = list(map(str,target))
    user_attempts = 0
    user_guess_list = []
    print(target)

    while user_guess_list != str_target:
        user_guess = input('Guess a four digit # or exit: ')
        user_guess_list = []
        user_attempts += 1
        cows = 0
        bulls = 0

        print()

        if user_guess == 'exit':
            exit()

        if len(user_guess) != 4:
            print('Please enter a 4 digit #')
            continue

        for i in range(0, 4):
            a = user_guess[i]
            user_guess_list.append(a)
            i += 1

        for x in range(0,4):
            if user_guess_list[x] == str_target[x]:
                cows += 1
                x += 1
            elif user_guess_list[x] in str_target:
                bulls += 1
                x += 1
            else: x += 1

        print('You have ' + str(bulls) + ' bulls')
        print('You have ' + str(cows) + ' cows')
        print('You have made ' + str(user_attempts) + ' guesses')
        print()

if __name__ == "__main__": main()