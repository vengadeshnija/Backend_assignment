from fastapi import FastAPI
import auth
import notes

app = FastAPI()

app.include_router(auth.router)
app.include_router(notes.router)
