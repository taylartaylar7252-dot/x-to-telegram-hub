from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "X-to-Telegram Smart Hub API is running"}
