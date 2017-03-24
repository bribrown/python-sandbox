# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this

import random

def main():

    #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    a = list(random.sample(range(1, 100), 18))
    a_index = list(range(0, len(a)))
    #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    e = list(random.sample(range(1, 100), 14))

    for i in a_index:
        x = a[i]
        if x in e and x not in c: c.append(x)

    print(c)
    print(a)
    print(e)

if __name__ == "__main__": main()