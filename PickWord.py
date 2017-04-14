#In this exercise, the task is to write a function that picks a random word from the file [sowpods.txt].

import random

def main():
    wl = []
    with open('sowpods.txt', 'r') as open_file:
        all_text = open_file.readline()
        while all_text:
            wl.append(all_text)
            all_text = open_file.readline()

    wlen = len(wl)-1
    random_word_index = random.randint(0,wlen)
    random_word = wl[random_word_index]

    print(random_word)

if __name__ == "__main__": main()

# with open('sowpods.txt') as f:
# 	words = list(f)
# print(random.choice(words).strip())