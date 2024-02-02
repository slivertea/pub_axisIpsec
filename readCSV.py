import csv

locations = []

fileCSV='importLocations.csv'
with open(fileCSV, mode = 'r') as fh:
    csvReader = csv.DictReader(fh)
    importData = [row for row in csvReader]
    for row in importData:
        locations.append(row["locationName"])

print (locations)
