import requests
import json
from dotenv import load_dotenv
import os
from colorama import init, Fore, Back, Style

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
print(results['main'])
print(results['main']['temp'])

print()
while True:
    try:
        print('What data would you like to see?: ' + Fore.GREEN + str(key_list),end='')
        print(Style.RESET_ALL,end='')
        x=input()
        print(results[x])
        break
    except:
        print('Enter a valid key.')
print()
