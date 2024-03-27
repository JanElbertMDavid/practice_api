
from sqlalchemy.orm.session import Session
from db.hash import Hash
from db.models import DbUser
from fastapi import HTTPException, status
from schemas import UserBase

#Creating a user
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    db.add(new_user) 
    db.commit()
    db.refresh(new_user)
    return new_user

#Reading a user's profile, from everyone to just one user
def get_all_users(db: Session):
    return db.query(DbUser).all()

def  get_user_by_username(db: Session, username: str):
    user = db.query(DbUser).filter(DbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail= f'User with username {username} not found')
    return user

#Updating the information of an existing user
def update_user(db:Session, id: int, request: UserBase):
    user = db.query(DbUser).filter(DbUser.id == id)
    user.update({
        DbUser.username: request.username,
        DbUser.email: request.email,
        DbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'Update Complete'

#Delete a specific user
def delete_user(db:Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    db.delete(user)
    db.commit()
    return 'Deleted the User'