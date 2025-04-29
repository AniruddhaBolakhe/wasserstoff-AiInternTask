# backend/api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from backend.core.ai_client import get_ai_verdict
from backend.core.game_logic import GameSession
from backend.core.moderation import is_clean
from backend.db.mongo import increment_guess_count, get_guess_count

router = APIRouter()
sessions = {}

class GuessRequest(BaseModel):
    session_id: str
    seed: str
    guess: str
    persona: str = "serious"

@router.post("/guess")
async def guess_word(req: GuessRequest):
    if not is_clean(req.guess):
        return {"verdict": "Inappropriate guess.", "score": 0, "history": []}

    game = sessions.setdefault(req.session_id, GameSession(seed=req.seed))

    if req.guess in game.values:
        return {
            "verdict": "Game Over! Duplicate guess.",
            "score": game.score,
            "history": game.history()
        }

    # Use only Gemini verdict (no Redis caching!)
    verdict = await get_ai_verdict(req.seed, req.guess, req.persona)

    if verdict == "yes":
        game.guess(req.guess)
        increment_guess_count(req.guess)
        total = get_guess_count(req.guess)
        game.seed = req.guess
        return {
            "verdict": f"✅ '{req.guess}' beats '{req.seed}'! Guessed {total} times.",
            "score": game.score,
            "history": game.history(),
            "next_seed": req.guess
        }

    return {
        "verdict": f"❌ '{req.guess}' does not beat '{req.seed}'.",
        "score": game.score,
        "history": game.history()
    }
