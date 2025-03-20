from pymongo import MongoClient
from config import Config
from passlib.context import CryptContext

client = MongoClient(Config.LOCAL_URI)
db = client['plugpoint']
pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")