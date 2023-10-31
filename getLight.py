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

stop= [

    r,w,w,w,w,w,w,r,

    w,r,w,w,w,w,r,w,

    w,w,r,w,w,r,w,w,

    w,w,w,r,r,w,w,w,

    w,w,w,r,r,w,w,w,

    w,w,r,w,w,r,w,w,

    w,r,w,w,w,w,r,w,

    r,w,w,w,w,w,w,r,

    ]

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

sense.set_pixels(stop)

time.sleep(0.5)
sense.set_pixels(one)

time.sleep(0.5)
sense.set_pixels(two)

time.sleep(0.5)
sense.set_pixels(three)

time.sleep(0.5)
sense.set_pixels(four)

time.sleep(0.5)

sense.show_message("Start")
#Connect to the database/collection
uri="mongodb+srv://username:password@cluster0.acgjcjc.mongodb.net"
client = MongoClient(uri)
db = client.frejs
coll = db.sensor_data
counter = 0

while(True):
    try:
        ljus = coll.find().sort("_id",-1).limit(1)
        for x in ljus:
            senaste=x["ljusstyrka"]
            print(senaste)
   
        if(int(senaste)<1000):
            #sense.show_message(str(senaste)+"a")
            sense.set_pixels(stop)
        elif(int(senaste)<5000):
            #sense.show_message(str(senaste)+"b")
            sense.set_pixels(one)
        elif(int(senaste)<15000):
            sense.set_pixels(two)
            #sense.show_message(str(senaste)+"c")
        elif(int(senaste)<25000):
            sense.set_pixels(three)
            #sense.show_message(str(ssenaste)+"d")
        else:
            sense.set_pixels(four)
        #sense.set_pixels(stop)
        time.sleep(3)
        counter +=1
        sense.clear()
        
    except ValueError:
        print("OH NO, Wrong value")
        sense.clear()
        client.close()
    except KeyboardInterrupt:
        sense.clear()
        print("exiting")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
