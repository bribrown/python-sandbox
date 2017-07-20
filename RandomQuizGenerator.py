# Project: Generating Random Quiz Files
#
# Say you’re a geography teacher with 35 students in your class and you want to give a pop quiz on US state capitals. Alas,
# your class has a few bad eggs in it, and you can’t trust the students not to cheat. You’d like to randomize the order of
# questions so that each quiz is unique, making it impossible for anyone to crib answers from anyone else. Of course, doing
# this by hand would be a lengthy and boring affair. Fortunately, you know some Python.

# Here is what the program does:
#
# Creates 35 different quizzes.
#
# Creates 50 multiple-choice questions for each quiz, in random order.
#
# Provides the correct answer and three random wrong answers for each question, in random order.
#
# Writes the quizzes to 35 text files.
#
# Writes the answer keys to 35 text files.
#
# This means the code will need to do the following:
#
# Store the states and their capitals in a dictionary.
#
# Call open(), write(), and close() for the quiz and answer key text files.
#
# Use random.shuffle() to randomize the order of the questions and multiple-choice options.

import random
import string

def main():
    capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
                'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
                'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
                'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
                'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
                'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
                'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
                'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
                'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
                'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
                'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
                'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
                'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
                'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

    # for k,v in capitals.items():
    #     print(v + ' ' + k)

    print()

    a = list(capitals.values())
    print(a)

    b = list(capitals.items())
    print(b)

    c = list(capitals.keys())
    print(c)

    # print()
    #
    # print(b[0][0])
    # print(b[0][1])
    # print(b[1][0])
    # print(b[1][1])

    # random.shuffle(b)
    #
    # print()
    # print(b)
    print()

    random.shuffle(b)
    for i in range(0,50):
        #random.shuffle(b)
        print('Question # ' + str(i+1) + ':' + ' What is the capital of: ' + b[i][0] + '?')
        print()
        rl = []
        t=0
        #for x in range(3):
        while t < 3:
            x = random.randint(0, 49)
            if x not in rl and x != i:
                rl.append(x)
                t += 1
            else:
                #print('Got a match')
                continue
        rl.append(i)
        #print(rl)
        random.shuffle(rl)
        for j in range(len(rl)):
            vvv = rl[j]
            print(b[vvv][1])
            j += 1
        print()
        print('Answer: ' + b[i][1])
        print()
        i += 1

    # WHY DO SOME ANSWER LISTS ONLY HAVE 3 CHOICES (2 wrong, 1 right) - perhaps this happens during build of "rl"
    # list. Duplicate discarded, loop moves on instead of populating a value

    # rl = []
    # for x in range(3):
    #     x = random.randint(0,49)
    #     if x not in rl:
    #         rl.append(x)
    #     else:
    #         continue
    # print(rl)

    # for q in range(100):
    #     #q = random.randint(3677777,5677777)
    #     #q = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    #     q = ''.join([random.choice(string.ascii_letters) for n in range(10)])
    #     print(q)


if __name__ == "__main__": main()