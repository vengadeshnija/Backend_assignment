from fastapi import APIRouter, HTTPException
from database import users_collection
from models import create_user
from jwt_handler import sign_jwt

router = APIRouter()

@router.post("/register")
def register(username: str, email: str, password: str):
    if users_collection.find_one({"email": email}):
        raise HTTPException(status_code=400, detail="Email already exists")
    user = create_user(username, email, password)
    users_collection.insert_one(user)
    return sign_jwt(user["user_id"])

@router.post("/login")
def login(email: str, password: str):
    user = users_collection.find_one({"email": email})
    if user and user["password"] == password:
        return sign_jwt(user["user_id"])
    raise HTTPException(status_code=401, detail="Invalid credentials")
