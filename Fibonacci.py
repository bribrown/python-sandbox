# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can
# use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonnaci seqence
# is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def main():

    def get_user_number(input_text='Please provide a number: '):
        return int(input(input_text))

    def gen_fib():
        x = get_user_number('Please provide Fibonnaci list length: ')
        y = 1
        fl = []

        if x == 0:
            fl = [0]
            print(fl)
            exit()

        if x == 1:
            fl = [1]
            print(fl)
            exit()

        if x == 2:
            fl = [1,1]
            print(fl)
            exit()

        if x > 2:
            fl = [1, 1]
            while y < x:
                fl.append(fl[y] + fl[y-1])
                y += 1
        print(fl)

    gen_fib()

if __name__ == "__main__": main()

# def fibonacci():
#     num = int(input("How many numbers that generates?:"))
#     i = 1
#     if num == 0:
#         fib = []
#     elif num == 1:
#         fib = [1]
#     elif num == 2:
#         fib = [1,1]
#     elif num > 2:
#         fib = [1,1]
#         while i < (num - 1):
#             fib.append(fib[i] + fib[i-1])
#             i += 1
#     return fib
# print(fibonacci())
# input()