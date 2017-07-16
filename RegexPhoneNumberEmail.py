# Copy text from clipboard, search for phone numbers and email addresses, paste them back to clipboard

import pyperclip
import re

def main():

    pn = '123-456-7890 as the phone number, 666-777-9999 ext. 324 as the phone number, asaasdasdqwedqwdqwdqwqwdqwdqwd 999444-3333x5555'

    foundPhoneNum = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code - ? means optional
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', re.VERBOSE)

    foundEmail = re.compile(r'''(
        [a-zA-Z0-9._%+-]+      # username [] defines a character class for regex
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
         )''', re.VERBOSE)

    y = foundPhoneNum.findall(pn)

    b = []

    f=0

    while f < 3:
        for i in range(1,7):
            a = y[f][i]
            b.append(a)
            i += 1
        c = ''.join(b)
        print(c)
        b = []
        f += 1

if __name__ == "__main__": main()

# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?                # area code
#     (\s|-|\.)?                        # separator
#     (\d{3})                           # first 3 digits
#     (\s|-|\.)                         # separator
#     (\d{4})                           # last 4 digits
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
#     )''', re.VERBOSE)
#
# The phone number begins with an optional area code, so the area code group is followed with a question mark. Since the area code can be just three digits
# (that is, \d{3}) or three digits within parentheses (that is, \(\d{3}\)), you should have a pipe joining those parts. You can add the regex comment
#
# # Area code to this part of the multiline string to help you remember what (\d{3}|\(\d{3}\))? is supposed to match.
#
# The phone number separator character can be a space (\s), hyphen (-), or period (.), so these parts should also be joined by pipes.
# The next few parts of the regular expression are straightforward: three digits, followed by another separator, followed by four digits.
# The last part is an optional extension made up of any number of spaces followed by ext, x, or ext., followed by two to five digits.