from datetime import datetime, timedelta
from jose import jwt
from config import JWT_SECRET

def sign_jwt(user_id: str):
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return {"access_token": token}

def decode_jwt(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
