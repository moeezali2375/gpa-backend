from pydantic import BaseModel, EmailStr


class UsersCreate(BaseModel):
    email: EmailStr
    password: str


class UsersRead(BaseModel):
    id: int
    email: EmailStr
    isVerified: bool

    class Config:
        orm_mode = True
