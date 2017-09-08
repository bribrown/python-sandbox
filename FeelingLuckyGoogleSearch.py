# enter search term
# pass search term to Google
# open top 5 links in browser

import webbrowser
import requests
import bs4
import re

def main():
    searchTerm = input('Enter the word of phrase you want to search on: ')
    searchList = searchTerm.split()
    searchTerm= '+'.join(searchList)
    print()

    requestContent = requests.get('https://www.google.com/search?q=' + searchTerm)
    requestContent.raise_for_status()
    searchObject = bs4.BeautifulSoup(requestContent.text, 'html.parser')

    searchElems = searchObject.select('.r a')

    for i in range(0,5):
        printHref = searchElems[i].get('href')
        printGoodHrefOne = re.sub('/url.q=','',printHref)
        printGoodHrefTwo = re.sub('&sa=U.*', '', printGoodHrefOne)
        webbrowser.open(printGoodHrefTwo)
        print(printGoodHrefTwo)
        i += 1

if __name__ == "__main__": main()