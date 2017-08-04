import re

def main():

    pattern = re.compile(r'\.| ')

    ml = 'The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.'
   # listMl = ml.split()
    reListML = pattern.split(ml)

    for i in reListML:
        if i == '':
            z = reListML.index(i)
            reListML[z] = '.'
        else:
            continue

    print(reListML)
    print()

    for i in reListML:
        if i == ('ADJECTIVE'):
            x = input('Please enter an ' + i + ' ')
            y = reListML.index(i)
            reListML[y] = x
        elif i in ('NOUN','VERB'):
            x = input('Please enter a ' + i + ' ')
            y = reListML.index(i)
            reListML[y] = x
        else:
            continue

    newList = ' '.join(reListML)

    newList = newList.replace(' .', '.')

    print()

    print(newList,end=' ')

    print()

if __name__ == "__main__": main()