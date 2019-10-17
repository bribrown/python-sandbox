import requests
import json
from dotenv import load_dotenv
import os
from colorama import init, Fore, Style
import sys

def return_data(key_list,results):
    while True:
        try:
            print('What data would you like to see?: ' + Fore.GREEN + str(key_list),end='')
            print(Style.RESET_ALL,end='')
            x=input()
            print(results[x])
        except:
            print('Enter a valid key.')
        more_weather(key_list, results)

def more_weather(key_list,results):
    moreweather = ''
    while moreweather != 'Y':
        moreweather = input('Would you like more weather data (y/n)?')
        moreweather = moreweather.upper()
        if moreweather == 'N':
            sys.exit()
        elif moreweather == 'Y':
            return_data(key_list,results)
        else:
            print()
            print('Please enter \'y\' or \'n\'')
            print()
            continue

def main():

    load_dotenv()
    init()

    APPID = os.getenv('APPID')

    address='http://api.openweathermap.org/data/2.5/weather'

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    parameters = {'id':'524901','APPID':APPID,'units':'imperial'}

    response = requests.post(address,headers=headers,params=parameters)

    response.raise_for_status()

    # Display the JSON results returned
    results = response.json()
    print(json.dumps(results))

    print()

    key_list=[]

    for key in results.keys():
        key_list.append(key)

    print(key_list)
    # print(results['main'])
    # print(results['main']['temp'])

    print()
    return_data(key_list,results)
    print()
    # play_again = ''
    # while play_again != 'Y':
    #     play_again = input('Would you like more weather data (y/n)?')
    #     play_again = play_again.upper()
    #     if play_again == 'N':
    #         exit()
    #     elif play_again == 'Y':
    #         return_data(key_list,results)
    #     else:
    #         print()
    #         print('Please enter \'y\' or \'n\'')
    #         print()
    #         continue

if __name__ == "__main__": main()