from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends
from repositories.user_repo import UserRepo
from db import get_db
from schemas.user_shemas import UserSchema
router = APIRouter()

@router.post("/signup")
def signup(db:Session = Depends(get_db)):
    user_repo = UserRepo(db)
    user_repo.add_user()
    return {"message": "User created"}

@router.post("/login")
def login():
    return {"message": "User logged in"}
