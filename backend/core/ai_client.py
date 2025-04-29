import os
import google.generativeai as genai
from dotenv import load_dotenv
# from backend.core.cache import get_cached_verdict, set_cached_verdict  ❌ disable redis cache

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def get_ai_verdict(seed, guess, persona="serious"):
    prompt = f"Hey Could you tell if '{guess}' beats '{seed}'? Reply only Yes or No!"

    # Disable Redis caching logic temporarily
    # cached = get_cached_verdict(seed, guess)
    # if cached:
    #     print("Returning cached verdict.")
    #     return cached

    try:
        response = model.generate_content(prompt)
        answer = (response.text or "").strip().lower()
        verdict = "yes" if "yes" in answer else "no"

        # Disable Redis caching write
        # set_cached_verdict(seed, guess, verdict)

        return verdict
    except Exception as e:
        print("Gemini API Error:", e)
        return "no"
