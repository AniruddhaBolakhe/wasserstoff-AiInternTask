from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

app = FastAPI(title="What Beats Rock?")

# ✅ Allow frontend origin (replace with your actual Vercel app URL)
origins = [
    "https://wasserstoff-ai-intern-task-nine.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # only your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
