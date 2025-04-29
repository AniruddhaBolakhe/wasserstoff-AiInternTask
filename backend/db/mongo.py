import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["genai_game"]
guess_counter = db["guess_counts"]

def increment_guess_count(word):
    guess_counter.update_one({"word": word}, {"$inc": {"count": 1}}, upsert=True)

def get_guess_count(word):
    doc = guess_counter.find_one({"word": word})
    return doc.get("count", 0) if doc else 0
