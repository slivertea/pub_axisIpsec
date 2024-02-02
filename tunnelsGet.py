import requests
import json
import os

TOKEN = os.getenv('AXIS_TOKEN')
apiToken = 'Bearer '+TOKEN
tunnelsUrl = "https://admin-api.axissecurity.com/api/v1.0/tunnels?pageSize=100&pageNumber=1"


payload = ""
headers = {
  'Authorization': apiToken
}

# parse the results text as json into an array - for tunnels and locations.
#  .. sublocations are available under locations
tunnels = (requests.request("GET", tunnelsUrl, headers=headers, data=payload).json())

#print the first dictionary index in the array
print (json.dumps(tunnels["data"][0]))

#print(response.text)
