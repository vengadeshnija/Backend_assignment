from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError
from config import JWT_SECRET
from jwt_handler import decode_jwt

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            try:
                payload = decode_jwt(credentials.credentials)
                return payload["user_id"]
            except JWTError:
                raise HTTPException(status_code=403, detail="Invalid token")
        raise HTTPException(status_code=403, detail="Invalid authorization")
