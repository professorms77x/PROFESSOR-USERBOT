from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from config import MURL
MONGO_URI = "MURL"
mongo = MongoClient(MONGO_URI)
db = mongo["Client"]

