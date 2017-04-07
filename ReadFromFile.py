# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and
# print out the results to the screen. I have a .txt file [nameslist.txt] for you, if you want to use it!
#
# Extra:
#
# Instead of using the .txt file from above (or instead of, if you want the challenge),
# take this .txt file [Training_01.txt], and count how many of each “category” of each image there are.
# This text file is actually a list of files corresponding to the SUN database scene
# recognition database, and lists the file directory hierarchy for the images.
# Once you take a look at the first line or two of the file, it will be clear which part
# represents the scene category. To do this, you’re going to have to remember a bit about
# string parsing in Python 3. I talked a little bit about it in this post.

def main():

    # read contents of file into a variable, print entire variable
    # with open('nameslist.txt', 'r') as open_file:
    #     all_text = open_file.read()
    #     print(all_text)


    # read contents of line into a variable, print that line
    # with open('nameslist.txt', 'r') as open_file:
    #     while open_file.readline():
    #         all_text = open_file.readline()
    #         print(all_text, end='')

    # counter_dict = {}
    # with open('nameslist.txt') as f:
    #     line = f.readline()
    #     while line:
    #         line = line.strip()
    #         if line in counter_dict:
    #             counter_dict[line] += 1
    #         else:
    #             counter_dict[line] = 1
    #         line = f.readline()
    #
    # print(counter_dict)
    #
    # names_keys = counter_dict.keys()
    # names_values = counter_dict.values()
    #
    # print()
    #
    # print(names_keys)
    # print(names_values)
    #
    # print()
    #
    # for pair in counter_dict.items():
    #     print(pair)

    category_count = {}
    with open('Training_01.txt', 'r') as open_file:
        all_text = open_file.readline()
        while all_text:
            x = all_text.find('/sun')
            y = all_text[3:x]
            if y in category_count:
                category_count[y] += 1
            else:
                category_count[y] = 1
            #    line = f.readline()
            all_text = open_file.readline()

    print(category_count)


if __name__ == "__main__": main()