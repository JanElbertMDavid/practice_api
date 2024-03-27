from fastapi import FastAPI
from database.db import engine
from models import model

app = FastAPI()

model.Base.metadata.create_all(engine)

@app.get("/")
def display():
    return{"message": "Hello World!"}