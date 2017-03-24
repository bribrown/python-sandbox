import re

def main():
    fh = open('542747672_edited_satisfied_by_2nd_parent_updated.txt')
    for line in fh:
       # client = re.search('Client', line)
        match = re.search('Ice', line)
        if match:
            print(line, end='')
     #   elif client:
     #       print(line, end='')

    # for line in fh:
    #     print(line, end='')

if __name__ == "__main__": main()
