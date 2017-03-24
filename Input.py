### ask user for name and age, tell them what year they turn 100

import datetime

def main():
    name = input('Give me your name: ')
    age = int(input('Give me your age: '))
    repeats = int(input('How many repeats would you like? '))
    x = 0
    now = datetime.datetime.now()
    years_til_100 = int(100 - age)
    current_year = int(now.year)
    will_be_100 = str(current_year + years_til_100)

    print(name + ' will be 100 in the year ' + will_be_100)

    print()

    while x < repeats:
        print(name + ' will be 100 in the year ' + will_be_100)
        x = x + 1



if __name__ == "__main__": main()