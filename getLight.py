from pymongo import MongoClient
import time
from sense_hat import SenseHat
sense = SenseHat()
r = (255,0,0)

o = (255,128,0)

y = (255,255,0)

g = (0,255,0)

c = (0,255,255)

b = (0,0,0)

p = (255,0,255)

n = (255,128,128)

w = (255,255,255)

k = (0,0,0)

one = [

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    g,b,b,b,b,b,b,b,

    g,b,b,b,b,b,b,b,

    g,b,b,b,b,b,b,b,

    ]

two = [

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,g,b,b,b,b,b,

    g,b,g,b,b,b,b,b,

    g,b,g,b,b,b,b,b,

    g,b,g,b,b,b,b,b,

    ]

three = [

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,g,b,b,b,

    b,b,g,b,g,b,b,b,

    g,b,g,b,g,b,b,b,

    g,b,g,b,g,b,b,b,

    g,b,g,b,g,b,b,b,

    ]

four = [

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,b,b,

    b,b,b,b,b,b,g,b,

    b,b,b,b,g,b,g,b,

    b,b,g,b,g,b,g,b,

    g,b,g,b,g,b,g,b,

    g,b,g,b,g,b,g,b,

    g,b,g,b,g,b,g,b,

    ]
five = [

    w,w,w,w,w,w,w,w,

    w,w,w,w,w,w,w,w,

    b,b,b,b,b,b,g,b,

    b,b,b,b,g,b,g,b,

    b,b,g,b,g,b,g,b,

    g,b,g,b,g,b,g,b,

    g,b,g,b,g,b,g,b,

    g,b,g,b,g,b,g,b,

    ]

#Connect to the database/collection
uri="mongodb+srv://username:password@cluster0.acgjcjc.mongodb.net"
client = MongoClient(uri)
db = client.frejs
coll = db.sensor_data
counter = 0

while(counter<25):
    try:
        ljus = coll.find().sort("_id",-1).limit(1)
        for x in ljus:
            senaste=x["ljusstyrka"]
            print(senaste)
   
        if(int(senaste)<1000):
            #sense.show_message(str(senaste)+"a")
            sense.set_pixels(one)
        elif(int(senaste)<5000):
            #sense.show_message(str(senaste)+"b")
            sense.set_pixels(two)
        elif(int(senaste)<15000):
            sense.set_pixels(three)
            #sense.show_message(str(senaste)+"c")
        elif(int(senaste)<25000):
            sense.set_pixels(four)
            #sense.show_message(str(senaste)+"d")


        time.sleep(5)
        counter +=1
    
    except ValueError:
        print("OH NO, Wrong value")
        client.close()
