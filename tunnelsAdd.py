import json
import requests
import os

TOKEN = os.getenv('VLAB_TOKEN')
apiToken = 'Bearer '+TOKEN
path = "https://admin-api.axissecurity.com/api/v1.0/"
# Use locationGet.py to collect this, or browser debug method "tunnels" matching the desired location
locationId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
method = 'tunnels/'
params = ''
uri = path+method

tunnels = {"API_location1"}

# Post  payload
# array test


headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}
# test subnet range

for row in tunnels:
    print ("Row:",row)
    tunnelName=row+" - Tunnel1"
    jsonPayload = {
        "name": tunnelName,
        "authenticationID":"zaphod@slivertea.com",
        "authenticationPSK":"itSa$ecr4t",
        "locationID": locationId
        }
    payload = json.dumps(jsonPayload)
    print (uri)
    response = requests.request("POST", uri, headers=headers, data=payload)
    print(response.text)
