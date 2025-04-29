# backend/core/ai_client.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")

async def get_ai_verdict(seed, guess, persona="serious"):
    prompt = (
        f"Hey, could you tell if '{guess}' beats '{seed}'? Reply only Yes or No! "
        f"Respond in a {persona} style."
    )

    try:
        response = await model.generate_content_async(prompt)
        answer = (response.text or "").strip().lower()
        verdict = "yes" if "yes" in answer else "no"
        return verdict
    except Exception as e:
        print("Gemini API Error:", e)
        return "no"
