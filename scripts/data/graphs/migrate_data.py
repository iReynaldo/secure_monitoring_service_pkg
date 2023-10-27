# mongodb://localhost:27017

import pymongo
import json
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.v4
collection = db.simulations
requesting = []

with open(
    "final/subprefix/rov-none/no-attack-relay/akamai/settings.json"
) as settings_file:
    with open(
        "final/subprefix/rov-none/no-attack-relay/akamai/results.json"
    ) as results_file:
        jsonObj = settings_file.read()
        resultsJSON = results_file.read()
        myDict = json.loads(jsonObj)
        results_dict = json.loads(resultsJSON)
        myDict["results"] = results_dict
        requesting.append(InsertOne(myDict))

result = collection.bulk_write(requesting)
client.close()
