import json

x ='{"account_payment_methods": [{"bill_first_name": "Tom", "bill_last_name": "West", "bill_company_name": "The Wine Emporium", "bill_address1": "125 N Main St", "bill_city": "Sebastopol", "bill_state_prov": "CA", "bill_country": "US", "bill_postal_cd": "95472", "bill_work_phone": "7078235200", "bill_email": "info@the-wine-emporium.com", "bill_birthdate": "1957-09-27", "pay_method_name": "Visa Select", "pay_method_description": "Visa Card", "pay_method_type": 1, "suffix": "1111", "cc_expire_mm": 6, "cc_expire_yyyy": 2018, "cc_type": "Visa", "status": 1, "payment_method_no": 1, "persistent_ind": 1, "from_date": "2016-05-13 19:15:21"}, {"bill_first_name": "API Metrics", "bill_last_name": "Test", "bill_company_name": "Wine Emprioum", "bill_address1": "575 Market St", "bill_address3": "San Francisco", "bill_city": "San Francisco", "bill_state_prov": "CA", "bill_country": "US", "bill_postal_cd": "94105", "bill_phone": "4155827810", "bill_cell_phone": "4155827810", "bill_work_phone": "4155827810", "bill_fax": "4155827810", "pay_method_name": "API Test", "client_payment_method_id": "APIMetrics Test", "pay_method_description": "Testing API Metrics", "pay_method_type": 1, "suffix": "1111", "cc_expire_mm": 5, "cc_expire_yyyy": 2019, "cc_type": "Visa", "status": 1, "payment_method_no": 2, "persistent_ind": 1, "from_date": "2016-05-23"}, {"bill_first_name": "Tom", "bill_last_name": "West", "bill_company_name": "The Wine Emporium", "bill_address1": "125 N Main St", "bill_city": "Sebastopol", "bill_state_prov": "CA", "bill_country": "US", "bill_postal_cd": "95472", "bill_work_phone": "7078235200", "bill_email": "info@the-wine-emporium.com", "bill_birthdate": "1957-09-27", "pay_method_name": "NETS Test", "pay_method_type": 20, "status": 1, "payment_method_no": 3, "persistent_ind": 1, "from_date": "2016-08-30 17:24:34"}], "error_code": 0, "error_msg": "OK"}'

y = json.loads(x)

print(y['account_payment_methods'][1]['bill_last_name'])

length_key = len(y['account_payment_methods'])
print(length_key)

i = 0

print()

while i < length_key:
    print(y['account_payment_methods'][i]['bill_last_name'])
    i += 1

print()

# ky = y.keys()
# print(ky)

# for key in y.keys():
#   print(key)

dkl = []

for key in y.keys():
  dkl.append(key)

print(dkl)
