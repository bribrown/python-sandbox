import requests
import os

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
os.chdir('C:\\Users\\bbrownholtz\\Desktop')
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
playFile.close()



