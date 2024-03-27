from fastapi import FastAPI
from database.db import engine
from models import model
from routers import user

app = FastAPI()

model.Base.metadata.create_all(engine)

app.include_router(user.router)


@app.get("/")
def display():
    return{"message": "Hello World!"}