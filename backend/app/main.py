from fastapi import FastAPI
from app.routers import categories, channels

app = FastAPI()

app.include_router(categories.router)
app.include_router(channels.router)

@app.get("/")
def read_root():
    return {"message": "X-to-Telegram Smart Hub API is running"}
