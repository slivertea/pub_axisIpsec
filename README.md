# pub_axisIpsec
This is a collection for automating injestion of ipsec locations, tunnels, and sub locations into HPE's Axis Atmos SSE

## Resources
* https://www.axissecurity.com/
* Axis Tunnels: https://docs.axissecurity.com/docs/atmos-cloud-api-tunnels#delete-a-tunnel
* Axis Locations: https://docs.axissecurity.com/docs/atmos-cloud-api-locations#delete-a-location

_Repository Files_
1. import*.csv - source files for location, tunnels, or sublocation
2. **Add.py - python for executing a raw add, non-existing data yet in Axis
3. **Get.py - python for collecting existing data already in Axis
   Sample sub componants
   readCSV.py -  sample csv read
   tokenOs.py -   sample host environment read for safely injesting the API Key


## Requirements
1. Axis management UI Admin access
2. Axis API write access for tunnels and ipsec locations.
3. python3
4. pytnon3 modules for "os, csv, requests, json

## values to replace
* All referencees to acme.local, acme.com, etc.  (all credentials are deliberately fictional to replace)
* All id values referenced "x"
* Any custom data sources in the csv files such as location name, sub location name, and subnets.
