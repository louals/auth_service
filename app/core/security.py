from dotenv import load_dotenv
load_dotenv()  # Load .env early

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import os

# Get the secret key from env, fail fast if missing
SECRET = os.getenv("JWT_SECRET")
if not SECRET:
    raise RuntimeError("JWT_SECRET environment variable is not set")

# Password hashing utils
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# OAuth2 scheme for token extraction from Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Create JWT token with expiration and role claims
def create_token(user_data: dict, expires: timedelta = timedelta(hours=2)) -> str:
    payload = {
        "sub": user_data["email"],
        "role": user_data.get("role", "user"),
        "exp": datetime.utcnow() + expires,
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

# Decode token and return user payload, else raise 401
async def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalide")

# Admin-only route dependency
async def admin_required(current_user: dict = Depends(get_current_user)) -> dict:
    if current_user.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user
