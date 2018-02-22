# Copy text from clipboard, search for phone numbers and email addresses, paste them back to clipboard

import pyperclip
import re

def main():

    pn = '123-456-7890 as the phone number, 666-777-9999 ext. 324 as the phone number, asaasdasdqwedqwdqwdqwqwdqwdqwd 999444-3333x5555'

    em = 'aso1123123 119### bribrown@yahoo.com 2131 dasd3wdwd3 brian.brownholtz@gmail.com adff2fwwef3r23 r2 23r 23r bbrownholtz@ariasystems.tv'

    no_object = 'aso1123123 119### bribrown@yahoo.com 2131 dasd3wdwd3 brian.brownholtz@gmail.com adff2fwwef3r23 r2 23r 23r bbrownholtz@ariasystems.tv'

    no_object_tuples = re.findall(r'([\w\.-]+)(@)([\w\.-]+)', no_object)
    print(no_object_tuples)

    print()



    foundPhoneNum = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code - ? means optional
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                       # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', re.VERBOSE)

    foundEmail = re.compile(r'''(
        ([a-zA-Z0-9._%+-]+)      # username [] defines a character class for regex
        (@)                      # @ symbol
        ([a-zA-Z0-9.-]+ )        # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
         )''',re.VERBOSE)

    y = foundPhoneNum.findall(pn)

    z = foundEmail.findall(em)

    print(y)
    print()
    print(z)
    print()



    # commented code, first element of findall (element 0) has whole expression
    # previous version of this code was taking elements > 0 and consolidating them
    # back into what already was available in element 0
    # b = []
    #
    f = 0
    #
    # while f < 3:
    #     for i in range(1,7):    # 6 possible elements in phone number
    #         a = y[f][i]
    #         b.append(a)
    #         i += 1
    #     c = ''.join(b)
    #     print(c)
    #     b = []
    #     f += 1

    plen = len(y)
    elen = len(z)

    print('Phone numbers found in string: {}'.format(plen))
    print()
    print('Email addresses found in string: {}'.format(elen))
    print()


    while f < plen:
        t = y[f][0]
        print(t)
        f += 1

    print()

    #w = []

    f = 0

    # while f < 3:
    #     for i in range(1,5):    # 4 possible elements in email
    #         a = z[f][i]
    #         w.append(a)
    #         i += 1
    #     d = ''.join(w)
    #     print(d)
    #     w = []
    #     f += 1

    while f < elen:
        r = z[f][0]
        print(r)
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