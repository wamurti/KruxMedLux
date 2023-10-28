from pymongo import MongoClient


uri="mongodb+srv://username:password@cluster0.acgjcjc.mongodb.net"
client = MongoClient(uri)

# database and collection code goes here

db = client.sample_guides

coll = db.comets
coll.drop()

# insert code goes here

docs = [

	{"name": "Halley's Comet", "officialName": "1P/Halley", "orbitalPeriod": 75, "radius": 3.4175, "mass": 2.2e14},

	{"name": "Wild2", "officialName": "81P/Wild", "orbitalPeriod": 6.41, "radius": 1.5534, "mass": 2.3e13},

	{"name": "Comet Hyakutake", "officialName": "C/1996 B2", "orbitalPeriod": 17000, "radius": 0.77671, "mass": 8.8e12},

    ]

result = coll.insert_many(docs)

# display the results of your operation

print(result.inserted_ids)


# Close the connection to MongoDB when you're done.

client.close()

# luxdata = {"lux":lux,"location":"sthlm"}
# objectid("").getTimestamp() will get you the timestamp if needed