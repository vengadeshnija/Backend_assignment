import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "notesapp")
JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
