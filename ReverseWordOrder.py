# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

def string_to_reverse():
    test_string = input('Please input a sentence: ')
    split_string = test_string.split(' ')
    split_string_index = len(split_string) - 1
    rebuilt_string = []

    while split_string_index >= 0:
        rebuilt_string.append(split_string[split_string_index])
        split_string_index -= 1

    print(rebuilt_string)

def main():

    string_to_reverse()

if __name__ == "__main__": main()