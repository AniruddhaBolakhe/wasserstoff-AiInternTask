from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

app = FastAPI(title="What Beats Rock?")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://wasserstoff-ai-intern-task-nine.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
