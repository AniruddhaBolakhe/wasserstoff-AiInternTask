import redis
import hashlib

redis_client = redis.Redis(host="redis", port=6379, db=0)

def make_cache_key(seed, guess):
    return hashlib.sha256(f"{seed.lower()}::{guess.lower()}".encode()).hexdigest()

def get_cached_verdict(seed, guess):
    value = redis_client.get(make_cache_key(seed, guess))
    return value.decode() if value else None

def set_cached_verdict(seed, guess, verdict):
    redis_client.set(make_cache_key(seed, guess), verdict, ex=3600)
