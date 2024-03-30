from sqlalchemy.orm.session import Session
from db.models import DbNote
from fastapi import HTTPException, status
from schemas import NoteBase

#Creating a note
def create_note(db: Session, request: NoteBase):
    new_note = DbNote(
        title = request.title,
        content = request.content,
        date_created = request.date_created
    )
    db.add(new_note) 
    db.commit()
    db.refresh(new_note)
    return new_note

#Reading a note
def get_all_notes(db: Session):
    return db.query(DbNote).all()

def  get_note_by_title(db: Session, title: str):
    title = db.query(DbNote).filter(DbNote.title == title).first()
    if not title:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail= f'Note with title {title} not found')
    return title

#Updating the information of the note
def update_note(db:Session, id: int, request: NoteBase):
    title = db.query(DbNote).filter(DbNote.id == id)
    title.update({
        DbNote.title: request.title,
        DbNote.content: request.content,
        DbNote.date_created: request.date_created
    })
    db.commit()
    return 'Update Complete'

#Delete a specific note
def delete_note(db:Session, id: int):
    note = db.query(DbNote).filter(DbNote.id == id).first()
    db.delete(note)
    db.commit()
    return 'Deleted the Note'