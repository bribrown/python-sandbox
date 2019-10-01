import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

auth_key = os.getenv('AUTHKEY')

#print(auth_key)

address='https://api.future.stage.ariasystems.net/api/ws/api_ws_class_dispatcher.php'

parameters = {'rest_call':'get_acct_payment_methods_and_terms_m',
'client_no':'6000093','auth_key':auth_key,'acct_no':'140671',
'output_format':'json'}

headers = {'Content-Type': 'application/x-www-form-urlencoded'}

response = requests.post(address,headers=headers,params=parameters)

response.raise_for_status()

# Display the JSON results returned
results = response.json()
print(json.dumps(results))