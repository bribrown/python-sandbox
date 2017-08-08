import re
import os
import random

def createMadLibList():
    madLibList = []
    os.chdir('C:\\Users\\bbrownholtz\\Desktop')
    with open('15_Sentences.txt', 'r') as open_file:
        all_text = open_file.readline()
        while all_text:
            all_text = all_text.strip()
            madLibList.append(all_text)
            all_text = open_file.readline()
    return madLibList

def main():

    getMadLibList = createMadLibList()
    random.shuffle(getMadLibList)

    ml = getMadLibList[0]

    pattern = re.compile(r'\.| ')

    reListML = pattern.split(ml)

    for i in reListML:
        if i == '':
            z = reListML.index(i)
            reListML[z] = '.'
        else:
            continue

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

    os.chdir('C:\\Users\\bbrownholtz\\Desktop')
    madLibsFile = open('madLib' + '.txt', 'a')
    madLibsFile.write(newList + '\n')
    madLibsFile.close()

    print()

if __name__ == "__main__": main()