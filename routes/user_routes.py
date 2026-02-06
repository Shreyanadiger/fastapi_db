from fastapi import APIRouter

router = APIRouter()

@router.post("/signup")
def signup():
    return {"message": "User created"}

@router.post("/login")
def login():
    return {"message": "User logged in"}
