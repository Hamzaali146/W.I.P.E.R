from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth_schema import (
    LoginRequest,
    SignupRequest,
    LoginResponse,
    SignupResponse,
)
from app.services.auth_service import authenticate_user, create_user
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", response_model=SignupResponse)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    user = create_user(db, payload.user_name, payload.email, payload.password)

    if not user:
        raise HTTPException(status_code=400, detail="Email already exists")

    return {
        "message": "User created successfully",
        "user": {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "email": user.email
        }
    }


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    result = authenticate_user(db, payload.email, payload.password)

    if not result:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return result