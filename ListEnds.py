# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and
# last elements of the given list. For practice, write this code inside a function.

def main():

    # def get_user_number(input_text='Please provide a number: '):
    #     return int(input(input_text))

    def build_list(a):
        list_length = len(a)
        end_index = list_length - 1
        new_list = []

        new_list.append(a[0])
        new_list.append(a[end_index])

        print(new_list)

    build_list([1,2,3,88,99,232])


if __name__ == "__main__": main()