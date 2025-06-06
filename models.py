from datetime import datetime
from uuid import uuid4

def create_user(username, email, hashed_password):
    return {
        "user_id": str(uuid4()),
        "username": username,
        "email": email,
        "password": hashed_password,
        "created_on": datetime.utcnow(),
        "last_update": datetime.utcnow()
    }

def create_note(title, content, user_id):
    return {
        "note_id": str(uuid4()),
        "title": title,
        "content": content,
        "user_id": user_id,
        "created_on": datetime.utcnow(),
        "last_update": datetime.utcnow()
    }
