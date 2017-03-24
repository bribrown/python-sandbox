# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

def main():

    x = int(input('Please enter a number to determine its divisors: '))
    y = 1
    a = []

    while y <= x:
        if x % y == 0: a.append(y)
        y = y + 1

    print(a)

if __name__ == "__main__": main()

# solution with range
#
# num = int(input("Please choose a number to divide: "))
#
# listRange = list(range(1,num+1))
#
# divisorList = []
#
# for number in listRange:
#     if num % number == 0:
#         divisorList.append(number)
#
# print(divisorList)