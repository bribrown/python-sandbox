import string
import random

def main():

    for q in range(100):
        #q = random.randint(3677777,5677777)
        #q = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
        q = ''.join([random.choice(string.ascii_letters) for n in range(10)])
        print(q)

if __name__ == "__main__": main()