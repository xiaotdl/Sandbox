import csv
import json
from collections import namedtuple, defaultdict

headers = ['Test', 'Endpoint', 'Method', 'Start_Time', 'End_Time', 'Total_Seconds']
EndpointRecord = namedtuple('EndpointRecord', headers)

data = defaultdict()
with open("in.csv", "rU") as f:
    csvreader = csv.reader(f)
    next(f) # skip header row
    for endpointRecord in map(EndpointRecord._make, csvreader):
        data.setdefault(endpointRecord.Test, []).append(endpointRecord)
# print json.dumps(data, indent=4)

with open('out.csv', 'wb') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    for test in data:
        endpointRecords = data[test]
        for endpointRecord in endpointRecords:
            row = []
            # nasty endpointRecord preparation
            for i in range(len(headers)):
                row.append(endpointRecord[i])
            csvwriter.writerow(row)
