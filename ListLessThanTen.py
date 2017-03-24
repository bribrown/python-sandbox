# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it
# and print out this new list.
#
# Write this in one line of Python.
#
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller
# than that number given by the user.

def main():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    c = int(input('Enter a number to compare to list: '))
    d = []

    for i in a:
        if i < 5: print(i)

    for i in a:
        if i < 5: b.append(i)

    print(b)

    for i in a:
        if i < c: d.append(i)

    print(d)

if __name__ == "__main__": main()