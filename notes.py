from fastapi import APIRouter, Depends, HTTPException
from database import notes_collection
from models import create_note
from jwt_bearer import JWTBearer

router = APIRouter()

@router.post("/note", dependencies=[Depends(JWTBearer())])
def add_note(title: str, content: str, user_id: str = Depends(JWTBearer())):
    note = create_note(title, content, user_id)
    notes_collection.insert_one(note)
    return {"msg": "Note created", "note_id": note["note_id"]}

@router.get("/notes", dependencies=[Depends(JWTBearer())])
def list_notes(user_id: str = Depends(JWTBearer())):
    notes = list(notes_collection.find({"user_id": user_id}, {"_id": 0}))
    return notes
