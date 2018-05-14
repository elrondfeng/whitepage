import requests
import json

street_line_1 = '5912 cactus valley'
city = 'Charlotte'
postal_code = '28277'
state_code='NC'
base_target_url = 'https://proapi.whitepages.com/3.0/location'
white_key="a4ef0bb2e2124bbfb532f9e9f1f3ffe9"


params = {
    'street_line_1': street_line_1,
    'city' : city,
    'postal_code': postal_code,
    'state_code':state_code,
    'api_key':white_key
}

response = requests.post(base_target_url,params=params,verify=False)

print('response url is : ' + response.url)

data=  response.json()

print(json.dumps(data, indent=4, sort_keys=True))