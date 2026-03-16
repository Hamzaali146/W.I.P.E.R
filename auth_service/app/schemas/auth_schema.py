from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class SignupRequest(BaseModel):
    user_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    user_id: int
    user_name: str
    email: EmailStr


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse


class SignupResponse(BaseModel):
    message: str
    user: UserResponse