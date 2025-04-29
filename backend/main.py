from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router

app = FastAPI()

# ✅ Allow frontend (Vercel) to talk to backend (Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or replace "*" with your Vercel domain for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
