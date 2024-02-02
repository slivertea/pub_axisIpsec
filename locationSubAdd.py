import json
import requests
import os

TOKEN = os.getenv('AXIS_TOKEN')
apiToken = 'Bearer '+TOKEN
path = "https://admin-api.axissecurity.com/api/v1.0/"
# Use locationGet.py to collect this, or browser debug method "locations" matching the desired location
locationId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
method = 'locations/'+locationId+'/sublocations'
params = ''
uri = path+method
locations = {}
tunnels = {}

# Post  payload
# array test
tstArray = ["API-location1a"]

headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}
# test subnet range
subRanges = ["10.0.99.0/24"]
for row in tstArray:
    print ("Row:",row)
    subname=row+"_sub1"
    jsonPayload = {
        "name":subname,
        "ipRanges": subRanges
    }
    payload = json.dumps(jsonPayload)
    print (uri)
    response = requests.request("POST", uri, headers=headers, data=payload)
    print(response.text)
