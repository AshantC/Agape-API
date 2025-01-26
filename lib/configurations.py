from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv(dotenv_path='.local.properties', override=True)
uri = os.getenv("URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.agape_dev
collection = db["test-data"]
