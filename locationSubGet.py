import requests
import json
import os

TOKEN = os.getenv('VLAB_TOKEN')
apiToken = 'Bearer '+TOKEN
locationsUrl = "https://admin-api.axissecurity.com/api/v1.0/locations?pageSize=100&pageNumber=1"


payload = ""
headers = {
  'Authorization': apiToken
}

# parse the results text as json into an array - for tunnels and locations.
#  .. sublocations are available under locations
locations = (requests.request("GET", locationsUrl, headers=headers, data=payload).json())

#print the first dictionary index in the array
#print (json.dumps(locations["data"][0]))

#print(response.text)

# collect details of all sublocations
for row in locations["data"]:
    locationId = row["id"]
    locationsUrl = "https://admin-api.axissecurity.com/api/v1.0/locations/"+locationId+"/sublocations?pageSize=100&pageNumber=1"
    headers = {
      'Authorization': apiToken
    }
    subLocations = (requests.request("GET", locationsUrl, headers=headers, data=payload).json())
    print (json.dumps(subLocations))
