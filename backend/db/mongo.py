from pymongo import MongoClient

db = MongoClient("mongodb://mongo:27017")["genai_game"]
guess_counter = db["guess_counts"]

def increment_guess_count(word):
    guess_counter.update_one({"word": word}, {"$inc": {"count": 1}}, upsert=True)

def get_guess_count(word):
    doc = guess_counter.find_one({"word": word})
    return doc.get("count", 0) if doc else 0
