from sqlmodel import Session, select
from ..models.usersModel import Users
from ..models.usersSchema import UsersCreate
from ..utils.passwordUtils import hash_password


def get_user_by_email(session: Session, email: str):
    statement = select(Users).where(Users.email == email)
    result = session.exec(statement).first()
    return result


def create_user(session: Session, user: UsersCreate):
    hashed_password = hash_password(user.password)
    db_user = Users(email=user.email, password=hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_all_users(session: Session):
    statement = select(Users)
    results = session.exec(statement).all()
    return results
