# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random

def main():

    # Function with SET
    #
    # def no_dup_list(x):
    #     y = set(x)
    #     print(y)
    #
    # no_dup_list([1,1,5,5,7,7])

    # Function with loop
    #
    # def no_dup_list(x):
    #     cl = []
    #     for i in x:
    #         if i not in cl: cl.append(i)
    #         else: continue
    #     print(cl)
    #
    # no_dup_list([1, 1, 5, 5, 7, 7])

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    #a = list(random.sample(range(1, 100), 18))
    a_index = list(range(0, len(a)))
    c = []
    e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #e = list(random.sample(range(1, 100), 14))

    for i in a_index:
        x = a[i]
        #if x in e and x not in c: c.append(x)
        if x in e: c.append(x)
        d=set(c)

    print(c)
    print(d)
    print(a)
    print(e)

if __name__ == "__main__": main()