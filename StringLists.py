# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

def main():

    evalstring = input('Enter string for palindrome evaluation: ')
    levalstring = list(evalstring)
    revalstring = evalstring[::-1]
    revlevalstring = list(revalstring)

    if levalstring == revlevalstring:
        print(evalstring + " is a palindrome")
    else:
        print(evalstring + " is not a palindrome")

if __name__ == "__main__": main()