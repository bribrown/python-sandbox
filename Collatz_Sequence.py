# https://automatetheboringstuff.com/chapter3/

# def collatz(num):
#     if num % 2 == 0:
#         print(str(num//2))
#     else:
#         print(str((3*num)+1))
#
# def main():
#     collatz(33)
#
# if __name__ == "__main__": main()

def collatz():
    num = input('Please enter a starting number: ')
    cycles = 1
    print()
    try:
        int(num)
    except ValueError:
        print('Only integers please')
        main()
    num = int(num)
    print(str(num), end = ', ')
    if num == 1:
        print('1 is the value we are looking for')
    while num != 1:
        if num // 2 == 1:
            print('1 is the value we are looking for')
            print()
            print('Number of cycles to get to 1: ' + str(cycles))
            exit()
        elif num % 2 == 0:
            print(str(num // 2), end = ', ')
            num = num // 2
            cycles += 1
        else:
            print(str((3*num)+1), end = ', ')
            num = ((3*num)+1)
            cycles += 1

def main():
    collatz()

if __name__ == "__main__": main()
