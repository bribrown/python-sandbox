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
import os


def makeQuiz(stateList,quizNum):
    os.chdir('C:\\Users\\bbrownholtz\\Desktop\\State_Quizes\\Quizes')
    quizFile = open('quiz#' + quizNum + '.txt', 'a')
    os.chdir('C:\\Users\\bbrownholtz\\Desktop\\State_Quizes\\Answers')
    answerFile = open('answers#' + quizNum + '.txt', 'a')
    b = list(stateList.items())
    random.shuffle(b)
    for i in range(0,50):
        print('Question # ' + str(i+1) + ':' + ' What is the capital of ' + b[i][0] + '?')
        quizFile.write('Question # ' + str(i+1) + ':' + ' What is the capital of ' + b[i][0] + '?\n')
        print()
        quizFile.write('\n')
        answerList = []
        t = 0
        while t < 3:
            x = random.randint(0, 49)
            if x not in answerList and x != i:
                answerList.append(x)
                t += 1
            else:
                continue
        answerList.append(i)
        random.shuffle(answerList)
        for j in range(len(answerList)):
            a = answerList[j]
            print(b[a][1])
            quizFile.write(b[a][1]+'\n')
            quizFile.write('\n')
            j += 1
        print()
        print('Answer: ' + b[i][1])
        os.chdir('C:\\Users\\bbrownholtz\\Desktop\\State_Quizes\\Answers')
        answerFile.write('Question ' + str(i+1) + ':' + b[i][1] + '\n')
        answerFile.write('\n')
        print()
        os.chdir('C:\\Users\\bbrownholtz\\Desktop\\State_Quizes\\Quizes')
        i += 1
    quizFile.close()
    answerFile.close()

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

    print()

    quizzes = 1

    while quizzes < 3:
        makeQuiz(capitals,str(quizzes))
        quizzes += 1


if __name__ == "__main__": main()