from fastapi import HTTPException, Depends, APIRouter
from sqlmodel import Session
from typing import List

from ..config.databaseConfig import get_session
from ..models.usersSchema import UsersCreate
from ..models.usersModel import Users
from ..crud.authCrud import create_user, get_user_by_email, get_all_users
from ..utils.passwordUtils import verify_password 
from ..utils.jwtUtils import create_access_token 

router = APIRouter()


@router.post("/register", response_model=Users)
async def register_user(
    user: UsersCreate, session: Session = Depends(get_session)
) -> Users:
    existing_user = get_user_by_email(session, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = create_user(session, user)
    return user


@router.post("/login")
async def login(user: UsersCreate):
    db_user = get_user_by_email(user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = create_access_token(data=)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users", response_model=List[Users])
async def get_users(session: Session = Depends(get_session)) -> List[Users]:
    users = get_all_users(session)
    return users
