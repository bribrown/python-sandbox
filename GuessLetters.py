# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly
# before losing).
#
# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise, write the logic that asks a player to guess a letter and displays
# letters in the clue word that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word.
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly! Don’t worry about choosing a word randomly or keeping track
# of the number of guesses the player has remaining - we will deal with those in a future exercise.

import re
import random

# pick random word function

def get_word():
    wl = []
    with open('sowpods.txt', 'r') as open_file:
        all_text = open_file.readline()
        while all_text:
            wl.append(all_text)
            all_text = open_file.readline()
    wlen = len(wl) - 1
    random_word_index = random.randint(0, wlen)
    random_word = wl[random_word_index]
    return (random_word)

def main():
    word = get_word()
    wordlen = len(word)
    guess_internal = '%' * wordlen
    guess_external = '_ ' * wordlen
    guess_list = []
    number_of_guesses = 0

    print()
    print('Welcome to Hangman')
    print('Word: ' + guess_external)
    print()

    while guess_internal != word:
        guess = input('Guess a letter, the word, or exit: ')
        print()
        guess = guess.upper()
        if len(guess) != 1:
            if guess == 'EXIT':
                exit()
            elif guess == word:
                print('You guessed the word!')
                exit()
            else:
                print('Your guess is incorrect, please try again')
                print()
                continue
        if guess in guess_list:
            print('Letter has already been guessed, please try again')
            print()
            continue
        guess_list.append(guess)
        number_of_guesses += 1
        if guess in word:
            print('Letter ' + guess + ' is in the word!')
            print()
            iter = re.finditer(guess, word)
            indexes = [x.start() for x in iter]
            guess_index = list(guess_internal)
            for i in indexes:
                guess_index[i] = guess
            guess_internal = ''.join(guess_index)
            guess_external = guess_internal.replace('%','_ ')
            for y in guess_list:
                if y in word:
                    guess_external = guess_external.replace(y,y + ' ')
            print(guess_external)
            print()
            print('Your guess list: ' + str(guess_list))
            print('Number of guesses: ' + str(number_of_guesses))
            print()
        else:
            print('Letter ' + guess + ' is not in the word, please guess again')
            print()
            print(guess_external)
            print()
            print('Your guess list: ' + str(guess_list))
            print('Number of guesses: ' + str(number_of_guesses))
            print()

    print('You guessed the word!')

if __name__ == "__main__": main()