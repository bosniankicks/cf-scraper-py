# cf-sc-raper-


1. A remake of https://github.com/zfcsoftware/cf-clearance-scraper/tree/main for a python based solution
2. Invokes a browser automation tool to open up a website with https://github.com/kaliiiiiiiiii/undetected-playwright-python
3. Sends back a useragent used and the token for scraping purposes


INSTRUCTIONS
1. Run server.py
2. Format your python request as shown below, please make sure to set the exec_path in get_cf and enable permissions if not running localhost.

import requests

url = 'http://localhost:5001/get_cf_clearance'
data = {'url': 'https://deliveroo.co.uk/login'}  # Replace with the target URL

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to get cf-clearance token: {response.text}")
