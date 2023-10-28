#mongoget.py
from pymongo import MongoClient

uri="mongodb+srv://uername:password@cluster0.acgjcjc.mongodb.net"
client = MongoClient(uri)


db = client.sample_guides

coll = db.comets
print("\n*********************\nPrint all and time")
# Det här retunerar allt i collection
for x in coll.find():
    print(x)
    print(x['_id'].generation_time)

print("\n*********************")

# Det här väljer ut vad som ska returneras, bara namn här.
# Tydligen namn och id om man inte specifikt skriver in "_id":0.
for x in coll.find({},{"_id":0,"name":1}):
    print(x)

print("\n*********************")

# Specifikt data, hela objektet med det namnet.
myquery = {"name": "Wild2"}
item = coll.find(myquery)
for x in item:
    print(x)


print("\n*********************")


# Sortera och plocka
# kommer sortera i omvänd alfabetisk ordning, 1 för alfabetisk
mydoc = coll.find().sort("name", -1)
for x in mydoc:
    print(x)

print("\n*********************\nBara sista\n")
# Plockar ut sista objektet i sorteringen.
# Och genom att skicka med key,["name"], får vi 'löst' värdet, "Wild2"
# Kanske nåt sånt man kan göra med Lux
mydoc = coll.find({},{"_id":0,"name":1}).sort("name", -1).limit(1)
for x in mydoc:
    print(x["name"])


print("\n*********************\n")
# kan även skrivas som detta.
# dom sorteras efter namn och man får bara med sista.
# sen kan man välja värde i print, ex radius
mydoc = coll.find().sort("name", -1).limit(1)
for x in mydoc:
    print(x["radius"])

# För Kruxmedlux
# Detta borde ge nylux det lux värde som senaste data har.
"""
mylux = coll.find().sort("timestamp", 1).limit(1)
for x in mydoc:
    nylux= x["lux"]
"""

# Såg att _id har en inbyggd timestamp
# Så man kan sortera efter _id, en sekunds precision.Så måste skapa ett obj i taget
"""
mylux = coll.find().sort("_id", 1).limit(1)
for x in mydoc:
    nylux= x["lux"]
"""


client.close()
