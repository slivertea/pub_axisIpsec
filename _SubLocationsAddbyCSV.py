import requests
import json
import os
import csv

#Define static values
TOKEN = os.getenv('AXIS_TOKEN')
locationsUrl = "https://admin-api.axissecurity.com/api/v1.0/locations?pageSize=100&pageNumber=1"
apiToken = 'Bearer '+TOKEN
payload = ""
headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}




# Import the CSV data
fileCSV='importSubLocations.csv'
with open(fileCSV, mode = 'r') as fh:
    csvReader = csv.DictReader(fh)
    importData = [row for row in csvReader]




#STEP1 - Collect existing Locations
# Collect the location data
locations = (requests.request("GET", locationsUrl, headers=headers, data=payload).json())
# parse the location data
locationDict = {}
for result in locations["data"]:
    print ("..........", result["name"])
    locationData = {"name": "","id": ""}
    locationDict[locationData["name"]] = {}
    locationData["name"] = result["name"]
    locationData["id"] = result["id"]
    #print (locationData)
    locationDict[locationData["name"]] = locationData




# STEP2 - validate and record location matches from import CSV
#Validate the import has a matching location, and assume false for reporting after.
results = {}
for importRow in importData:
    results[importRow["subLocationName"]] = {"apiResponse": None, "isValidParent": False, "locationId": None, "subLocationName": importRow["subLocationName"],"inputData": importRow, "resultDetails": None}
    if importRow["parentLocationName"] in locationDict.keys():
        subLocationName = importRow["parentLocationName"]
        results[importRow["subLocationName"]]["isValidParent"] = True
        results[importRow["subLocationName"]]["locationId"] = locationDict[subLocationName]["id"]
        results[importRow["subLocationName"]]["subLocationName"] = importRow["subLocationName"]
#print (json.dumps(results))




# STEP3 - push sublocation additions for every valid result
for key in results:
    if results[key]["isValidParent"]:
        locationId = results[key]["locationId"]
        subName = results[key]["subLocationName"]
        subSubnets = [str(results[key]["inputData"]["subLocationSubnet"])]
        print ("subnets:", subSubnets)
        subBody = {
            "name":subName,
            "ipRanges": subSubnets
        }

        path = "https://admin-api.axissecurity.com/api/v1.0/"
        method = 'locations/'+locationId+'/sublocations'
        uri = path+method
        subPayload = json.dumps(subBody)
        headers = {
            'Authorization': apiToken,
            'Content-Type': 'application/json'
        }
        print ("Adding ", subName)
        response = requests.request("POST", uri, headers=headers, data=subPayload)
        results[key]["apiResponse"] = response.status_code
        results[key]["resultDetails"] = response.text
    else:
        print ("...Skipping", results[key]["subLocationName"], ": invalid location given in csv input")

print ("Complete Results:")
print (json.dumps(results))
