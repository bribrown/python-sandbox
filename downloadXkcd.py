# Download all xkcd comics to a folder
# indicates no more previous comics...https://xkcd.com/1/#

import requests
import bs4
import os

def main():

    # url = '//xkcd.com/'
    url = '//xkcd.com/1665/'

    while url != '//xkcd.com/1/#':
        comicRequest = requests.get('http:' + url)
        comicRequest.raise_for_status()

        soup = bs4.BeautifulSoup(comicRequest.text, 'html.parser')

        comicLink = soup.select('#comic img')
        try:
            comicLink = comicLink[0].get('src')
        except IndexError:
            comicLink = 'Cannot download comic'
            pass

        url = soup.select('.comicNav a')
        url = '//xkcd.com' + url[1].get('href')

        print('Current Link: ' + comicLink)
        print('Previous Link: ' + url)

    # comicUrl = 'http:' + comicLink
    # res = requests.get(comicUrl)
    # res.raise_for_status()

    # os.chdir('C:\\Users\\bbrownholtz\\Desktop')
    # comicFile = open('1.png', 'wb')
    # for chunk in res.iter_content(100000):
    #        comicFile.write(chunk)
    # comicFile.close()


if __name__ == "__main__": main()