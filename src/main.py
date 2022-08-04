from fastapi import FastAPI
from src.routers import markov

app = FastAPI()
app.include_router(markov.router)


@app.get("/")
async def root():
    return {"message": "ok"}


@app.get("/hello")
async def hello():
    return {"message": "Hello World"}
