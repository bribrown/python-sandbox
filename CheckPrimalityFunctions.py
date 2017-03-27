# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number
# that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions.

# from exercise 4
#
# def main():
#
#     x = int(input('Please enter a number to determine its divisors: '))
#     y = 1
#     a = []
#
#     while y <= x:
#         if x % y == 0: a.append(y)
#         y = y + 1
#
#     print(a)
#
# if __name__ == "__main__": main()

# function example:

def main():

    def get_user_number(input_text='Please provide a number: '):
        return int(input(input_text))

    g = get_user_number('Please provide a number greater than 2: ')
    d = 2

    print()

    if g <= 2:
        print('Please enter a number larger than 2')
        print()
        main()

    while d < g:
        if g % d != 0:
            d += 1
            continue
        elif g % d == 0:
            print(str(g) + ' is not a prime number')
            exit()
    print(str(g) + ' is a prime number')

if __name__ == "__main__": main()

# def main():
#
#     def get_integer(help_text="Give me a number: "):
#         return int(input(help_text))
#
#     age = get_integer("Tell me your age: ")
#     school_year = get_integer()
#     if age > 15:
#         print("You are over the age of 15")
#         print("You are in grade " + str(school_year))
#
# if __name__ == "__main__": main()


#using multiple functions:
#
# def get_number(prompt):
#     '''Returns integer value for input. Prompt is displayed text'''
#     return int(input(prompt))
#
#
# def is_prime(number):
#     '''Returns True for prime numbers, False otherwise'''
#     # Edge Cases
#     if number == 1:
#         prime = False
#     elif number == 2:
#         prime = True
#     # All other primes
#     else:
#         prime = True
#         for check_number in range(2, (number / 2) + 1):
#             if number % check_number == 0:
#                 prime = False
#                 break
#     return prime
#
#
# def print_prime(number):
#     prime = is_prime(number)
#     if prime:
#         descriptor = ""
#     else:
#         descriptor = "not "
#     print(number, " is ", descriptor, "prime.", sep="", end="\n\n")
#
#
# # never ending loop
#
# while 1 == 1:
#     print_prime(get_number("Enter a number to check. Ctl-C to exit."))