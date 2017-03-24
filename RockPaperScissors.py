# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock

def main():
    p1 = input('Player 1 value: ')

    allowed_values = ['Rock', 'Paper', 'Scissors']

    if p1 not in allowed_values:
        print('That value is not allowed')
        exit()

    p2 = input('Player 2 value: ')

    if p2 not in allowed_values:
        print('That value is not allowed')
        exit()

    if p1 == p2:
        print('Tie game')
        exit()

    print()

    if p1 == 'Rock' and p2 == 'Scissors':
        print('Player 1 wins')
    elif p1 == 'Rock' and p2 == 'Paper':
        print('Player 2 wins')
    elif p1 == 'Paper' and p2 == 'Rock':
        print('Player 1 wins')
    elif p1 == 'Paper' and p2 == 'Scissors':
        print('Player 2 wins')
    elif p1 == 'Scissors' and p2 == 'Rock':
        print('Player 2 wins')
    elif p1 == 'Scissors' and p2 == 'Paper':
        print('Player 1 wins')

    play_again = input('Play again (Y/N)?')
    str.capitalize(play_again)

    if play_again == 'N':
        exit()
    elif play_again == 'Y':
        print()
        main()
    else:
        exit()

if __name__ == "__main__": main()