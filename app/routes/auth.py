from fastapi import APIRouter, HTTPException
from app.models.user import User, UserLogin
from app.db import db
from app.core.security import hash_password, verify_password, create_token

router = APIRouter()

@router.post("/auth/signup")
async def signup(user: User):
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(400, "Email déjà utilisé.")
    user_data = user.dict()
    user_data["password"] = hash_password(user.password)
    if user_data.get("role") != "admin":
        user_data["role"] = "user"

    # Add default fields here so no missing keys later
    user_data["scoreTotal"] = 0
    user_data["partiesJouees"] = 0

    await db.users.insert_one(user_data)
    return {"message": "Compte créé"}


@router.post("/auth/login")
async def login(user: UserLogin):
    user_db = await db.users.find_one({"email": user.email})
    if not user_db or not verify_password(user.password, user_db["password"]):
        raise HTTPException(401, "Email ou mot de passe incorrect.")
    token = create_token(user_db)
    return {"access_token": token, "token_type": "bearer","username": user_db.get("username", user_db["email"]) , "role": user_db.get("role", "user")}
