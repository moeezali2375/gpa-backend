from typing import Optional
from sqlmodel import SQLModel, Field


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password: str
    isVerified: bool = Field(default=True)