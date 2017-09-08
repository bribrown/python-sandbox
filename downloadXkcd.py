# Download all xkcd comics to a folder
# indicates no more previous comics...https://xkcd.com/1/#

import requests
import bs4
import re
import os

def main():

    comicRequest = requests.get('http://xkcd.com/')
    comicRequest.raise_for_status()

    soup = bs4.BeautifulSoup(comicRequest.text, 'html.parser')

    comicLink = soup.select('#comic img')
    comicLink = comicLink[0].get('src')

    prevLink = soup.select('.comicNav a')
    prevLink = '//xkcd.com' + prevLink[1].get('href')

    print(comicLink)
    print(prevLink)

    comicUrl = 'http:' + comicLink
    res = requests.get(comicUrl)
    res.raise_for_status()

    # os.chdir('C:\\Users\\bbrownholtz\\Desktop')
    # comicFile = open('1.png', 'wb')
    # for chunk in res.iter_content(100000):
    #        comicFile.write(chunk)
    # comicFile.close()


if __name__ == "__main__": main()