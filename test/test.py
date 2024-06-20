import requests

url = 'http://localhost:5001/get_cf_clearance'
#used deliveroo for the interstit test
data = {'url': 'https://deliveroo.co.uk/login'}

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Failed to get cf_clearance token: {response.text}")
