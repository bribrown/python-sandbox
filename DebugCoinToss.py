import random
import logging

#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(level=logging.ERROR, format=' %(asctime)s - %(levelname)s - %(message)s') # only show ERROR messages
logging.basicConfig(filename='C:\\Users\\bbrownholtz\\Desktop\\loggingerrors.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# logging.disable(logging.DEBUG) - show only messages at higher level than DEBUG
# logging.disable(logging.ERROR) - show only messages at higher level than ERROR
# logging.disable(logging.CRITICAL) - disable all logging

logging.debug('Start of program')

guess = ''
while guess not in ('heads', 'tails'):
    logging.debug('Guess starts here')
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    logging.error('Guess is ' + guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads
#assert toss in ('heads','tails'), 'Toss is not heads or tails'
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')