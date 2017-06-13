# Say you have a list value like this:
#
#
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by
# a comma and a space, with and inserted before the last item. For example, passing the previous spam list to
# the function would return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.

def list_to_string(lts):
    len_lts = (len(lts)-1)
    i = 0
    while i < len_lts:
        print(lts[i], end = ', ')
        i += 1
    print('and ' + lts[len_lts] + '''''')

def main():
    tl = ['apples', 'bananas', 'tofu', 'cats', 'red', 'green', 'blue']
    list_to_string(tl)

if __name__ == "__main__": main()