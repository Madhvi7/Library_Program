from pymongo import MongoClient

MONGO_URI = "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
client = None
try:
    client = MongoClient(MONGO_URI)
    print("connected")
except Exception as e:
    print("default"+str(e))

# Creating database
db = client.interns_b2_23

# # Creating document
lib = db.Madhvi_lib


