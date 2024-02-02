import json
import requests
import os

TOKEN = os.getenv('AXIS_TOKEN')
apiToken = 'Bearer '+TOKEN
path = "https://admin-api.axissecurity.com/api/v1.0/"
method = 'tunnels/'
params = ''
locationId = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
uri = path+method
locations = {}
tunnels = {}

# Post  payload example
jsonPayload = {
"name":"API_location1 - Tunnelzz",
"authenticationID":"zaphod@acme.com",
"authenticationPSK":"itSa$ecr4t",
locationId
}

payload = json.dumps(jsonPayload)

headers = {
  'Authorization': apiToken,
  'Content-Type': 'application/json'
}
print (uri)
response = requests.request("POST", uri, headers=headers, data=payload)

print(response.text)
