from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
MONGO_URI = "mongodb+srv://riyihe1925:mIroEVXcVCGGwAFK@cluster0.g6ojimu.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(MONGO_URI)
db = mongo["Client"]

