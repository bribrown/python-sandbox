# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
#
# Extras:
#
# If the number is a multiple of 4, print out a different message.
#
# Ask the user for two numbers: one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

def main():
    num1 = float(input('Provide a number: '))
    result1 = num1 % 2
    result2 = num1 % 4

    if result1 == 0 and result2 == 0:
        print('Number ' + str(num1) + ' is even and divisible by 4')
    elif result1 == 0 and result2 != 0:
        print('Number ' + str(num1) + ' is even but not divisible by 4')
    else:
        print('Number ' + str(num1) + ' is odd')

if __name__ == "__main__": main()