from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):  #Class for user display
   username: str  # Username attribute
   email: str  # Email attribute
   class Config():  # Configuration for model
       orm_mode = True  # Allows use of ORM objects

class NoteBase(BaseModel):
    title: str
    content: str
    date_created: str

class NoteDisplay(BaseModel):
    title: str
    email: str
    class  Config():
        orm_mode = True