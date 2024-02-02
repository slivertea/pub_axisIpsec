import json
import requests
import os

TOKEN = os.getenv('AXIS_TOKEN')
apiToken = 'Bearer '+TOKEN
path = "https://admin-api.axissecurity.com/api/v1.0/"
method = 'commit/'
uri = path+method

# No Payload Necessary

headers = {
  'Authorization': apiToken,
  'Content-Type': 'application/json'
}
print (uri)
response = requests.request("POST", uri, headers=headers)

print(response.text)
