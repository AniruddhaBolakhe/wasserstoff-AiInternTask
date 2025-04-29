from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="What Beats Rock?")
app.include_router(router)
