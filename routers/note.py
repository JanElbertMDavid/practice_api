from schemas import NoteBase, NoteDisplay
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_note

router = APIRouter(
    prefix='/note',
    tags=['note']
)

#Create note
@router.post('/', response_model=NoteDisplay)
def create_note(request: NoteBase, db: Session = Depends(get_db)):
    #Exceptions are still here, lurking
    return db_note.create_note(db, request)

#Read all notes
@router.get('/', response_model=list[NoteDisplay])
def get_all_notes(db:Session=Depends(get_db)):
    #Exceptions are still here, lurking
    return db_note.get_all_notes(db)

#Read one note
@router.get('/{id}',response_model=NoteDisplay)
def get_note(id:int, db: Session = Depends(get_db)):
    return db_note.get_note_by_title(db, id)

#Update note
@router.post('/{id}/update')
def update_note(id: int, request: NoteBase, db: Session = Depends(get_db)):
    #Exceptions are still here, lurking
    return db_note.update_note(db, id, request)

#Delete note
@router.get('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    #Exceptions are still here, lurking
    return db_note.delete_note(db, id)