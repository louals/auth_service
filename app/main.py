from fastapi import FastAPI
from app.routes.auth import router as auth_router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()  

app = FastAPI(
    title="Auth Service",
    description="Microservice pour l'authentification (signup, login)",
    version="1.0.0"
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or "*" to allow all for dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusion des routes
app.include_router(auth_router, prefix="")

# Optionnel : une route de test pour vérifier que le service est UP
@app.get("/")
def read_root():
    return {"message": "Auth service is running ✅"}
