import re
import random

# function to pick random word

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

# function to handle if player wants to play again after game ends

def play_again_query():
    play_again = ''
    while play_again != 'Y':
        play_again = input('Would you like to play again (y/n)?')
        play_again = play_again.upper()
        if play_again == 'N':
            exit()
        elif play_again == 'Y':
            main()
        else:
            print()
            print('Please enter \'y\' or \'n\'')
            print()
            continue

def main():
    word = get_word().strip()
    wordlen = len(word)
    guess_internal = '%' * wordlen
    guess_external = '_ ' * wordlen
    guess_list = []
    number_of_incorrect_guesses = 0

    print()
    print('Welcome to Hangman')
    print('You are allowed 6 incorrect guesses.')
    print()
    print('Word: ' + guess_external)
    print()

    while guess_internal != word and number_of_incorrect_guesses <= 6:
        guess = input('Guess a letter, the word, or exit: ')
        print()
        guess = guess.upper()
        if len(guess) != 1:
            if guess == 'EXIT':
                exit()
            elif guess == word:
                print('You guessed the word!')
                print()
                play_again_query()
            else:
                print('Your guess is incorrect, please try again')
                print()
                continue
        if guess in guess_list:
            print('Letter has already been guessed, please try again')
            print()
            continue
        guess_list.append(guess)
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
            print('Number of incorrect guesses: ' + str(number_of_incorrect_guesses))
            print()
        else:
            number_of_incorrect_guesses += 1
            print('Letter ' + guess + ' is not in the word, please guess again')
            print()
            print(guess_external)
            print()
            print('Your guess list: ' + str(guess_list))
            print('Number of incorrect guesses: ' + str(number_of_incorrect_guesses))
            print()

    if guess_internal == word:
        print('You guessed the word!')
        print()
        play_again_query()

    print('You are out of incorrect guesses')
    print()
    print('The word was: ' + word)
    print()
    play_again_query()

if __name__ == "__main__": main()

# """
# Practice Python exercise 32
# Hangman
# http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
# """
#
# import random
#
# def pick_random_word():
# 	"""
# 	This function picks a random word from the SOWPODS
# 	dictionary. 
# 	"""
# 	# open the sowpods dictionary
# 	with open("sowpods.txt", 'r') as f:
# 		words = f.readlines()
#
# 	# generate a random index
# 	# -1 because len(words) is not a valid index into the list `words`
# 	index = random.randint(0, len(words) - 1)
#
# 	# print out the word at that index
# 	word = words[index].strip()
# 	return word
#
#
# def ask_user_for_next_letter():
# 	letter = input("Guess your letter: ")
# 	return letter.strip().upper()
#
#
# def generate_word_string(word, letters_guessed):
# 	output = []
# 	for letter in word:
# 		if letter in letters_guessed:
# 			output.append(letter.upper())
# 		else:
# 			output.append("_")
# 	return " ".join(output)
#
#
# if __name__ == '__main__':
# 	WORD = pick_random_word()
#
# 	letters_to_guess = set(WORD)
# 	correct_letters_guessed = set()
# 	incorrect_letters_guessed = set()
# 	num_guesses = 0
#
# 	print("Welcome to Hangman!")
# 	while (len(letters_to_guess) > 0) and num_guesses < 6:
# 		guess = ask_user_for_next_letter()
#
# 		# check if we already guessed that
# 		# letter
# 		if guess in correct_letters_guessed or \
# 				guess in incorrect_letters_guessed:
# 			# print out a message
# 			print("You already guessed that letter.")
# 			continue
#
# 		# if the guess was correct
# 		if guess in letters_to_guess:
# 			# update the letters_to_guess
# 			letters_to_guess.remove(guess)
# 			# update the correct letters guessed
# 			correct_letters_guessed.add(guess)
# 		else:
# 			incorrect_letters_guessed.add(guess)
# 			# only update the number of guesses
# 			# if you guess incorrectly
# 			num_guesses += 1
#
# 		word_string = generate_word_string(WORD, correct_letters_guessed)
# 		print(word_string)
# 		print("You have {} guesses left".format(6 - num_guesses))
#
# 	# tell the user they have won or lost
# 	if num_guesses < 6:
# 		print("Congratulations! You correctly guessed the word {}".format(WORD))
# 	else:
# 		print("Sorry, you list! Your word was {}".format(WORD))