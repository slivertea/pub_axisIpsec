import json
import requests
import os

TOKEN = os.getenv('AXIS_TOKEN')
apiToken = 'Bearer '+TOKEN
path = "https://admin-api.axissecurity.com/api/v1.0/"
method = 'locations/'
params = ''
uri = path+method
locations = {}


# Adding new locations
locations = ["API Location1a", "API Location2a", "API Location1c"]
# To import by CSV, uncomment the following section, and add contents to importLocations.csv file:
#locations = []
#fileCSV='importLocations.csv'
#with open(fileCSV, mode = 'r') as fh:
#    csvReader = csv.DictReader(fh)
#    importData = [row for row in csvReader]
#    for row in importData:
#        locations.append(row["locationName"])


headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}
for row in locations:
    print ("Row:",row)
    jsonPayload = {
        "name":row
    }
    payload = json.dumps(jsonPayload)
    print (uri)
    response = requests.request("POST", uri, headers=headers, data=payload)
    print(response.text)
