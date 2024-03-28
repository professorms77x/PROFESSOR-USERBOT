from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
MONGO_URI = "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority"
mongo = MongoClient(MONGO_URI)
db = mongo["Client"]
