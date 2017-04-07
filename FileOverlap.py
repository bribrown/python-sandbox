# Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One .txt
# [primenumbers.txt] file has a list of
# all prime numbers under 1000, and the other .txt file [happynumbers.txt] has a list of happy numbers up to 1000.

def main():
    hn = []
    fl = []
    eval_num = 0

    with open('happynumbers.txt', 'r') as openhl_file:
        while openhl_file.readline():
            happy_numbers = openhl_file.readline()
            happy_numbers = happy_numbers.strip()
            hn.append(happy_numbers)

    with open('primenumbers.txt', 'r') as openpn_file:
        while openpn_file.readline():
            eval_num = openpn_file.readline()
            eval_num = eval_num.strip()
            if eval_num in hn:
                fl.append(eval_num)
            else:
                continue

        print(fl)


if __name__ == "__main__": main()

# def filetolistofints(filename):
# 	list_to_return = []
# 	with open(filename) as f:
# 		line = f.readline()
# 		while line:
# 			list_to_return.append(int(line))
# 			line = f.readline()
# 	return list_to_return
#
# primeslist = filetolistofints('primenumbers.txt')
# happieslist = filetolistofints('happynumbers.txt')
#
# overlaplist = [elem for elem in primeslist if elem in happieslist]
# print(overlaplist)