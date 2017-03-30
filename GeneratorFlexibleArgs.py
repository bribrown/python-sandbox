def main():
    for i in inclusive_range(5,25):
        print(i, end=' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('More than 1 number needs to entered')
    elif numargs == 1:
        stop = args[0]
        start = 0
        step = 1
    elif numargs == 2:
        (start, stop) = args
        step = 1
    elif numargs == 3:
        (start, stop, step) = args
    else: raise TypeError('Only between 1 and 3 numbers can be entered')
    i = start
    while i <= stop:
        yield i
        i += step

if __name__ == "__main__": main()