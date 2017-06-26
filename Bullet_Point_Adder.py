# The bulletPointAdder.py script will get the text from the clipboard,
# add a star and space to the beginning of each line, and then paste this new text to the clipboard.

import pyperclip

def main():

    ClipText = pyperclip.paste()
    ClipText = ClipText.split('\n')
    i = 0

    for i in range(len(ClipText)):
        ClipText[i] = ('* ' + ClipText[i]).rstrip()
        i += 1

    ClipText = '\n'.join(ClipText)

    #print(ClipText)
    pyperclip.copy(ClipText)

if __name__ == "__main__": main()