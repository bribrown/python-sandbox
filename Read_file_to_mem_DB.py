import json
import os
import sqlite3

def main():

    os.chdir('C:\\Users\\bbrownholtz\\PycharmProjects\\Sandbox\\city.list.json')
    with open('edited.city.list.json') as f:
        data = json.load(f)

    connectionObject = sqlite3.connect(":memory:")

    cursorObject = connectionObject.cursor()

    createTable = "CREATE TABLE CITIES (id int, Name varchar(32), Country varchar(32))"

    cursorObject.execute(createTable)

    i=0

    while i < len(data):
            cursorObject.execute("INSERT INTO CITIES values (?, ?, ?)", ((data[i]['id']), data[i]['name'], data[i]['country']))
            i += 1

    user_country = input('What country are you interested in?: ')

    cmd = "SELECT * from CITIES WHERE country like '{}'".format(user_country)
    queryResults=cursorObject.execute(cmd)

    for result in queryResults:
          print(result)

    print()

    cmd = "SELECT distinct(country) from CITIES"
    queryResults = cursorObject.execute(cmd)

    # for result in queryResults:
    #     print(result)

    country_list=[]

    for result in queryResults:
        country_list.append(result[0])
    print(country_list)
    #print(str(len(country_list)))

    connectionObject.close()

if __name__ == "__main__": main()