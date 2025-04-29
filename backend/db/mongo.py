# backend/db/mongo.py

from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load .env file for local development
load_dotenv()

# Get the MongoDB URI from the environment
MONGO_URI = os.getenv("MONGO_URI")

# Set up MongoDB client with TLS (SSL) flags
client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsAllowInvalidCertificates=True
)

# Access your database and collection
db = client["game"]             # You can change "game" to your DB name
collection = db["guesses"]      # You can change "guesses" to your collection name


def increment_guess_count(word: str):
    """Increment the count of how many times a word has been guessed."""
    collection.update_one(
        {"word": word},
        {"$inc": {"count": 1}},
        upsert=True
    )


def get_guess_count(word: str) -> int:
    """Get the number of times a word has been guessed."""
    doc = collection.find_one({"word": word})
    return doc["count"] if doc else 0
