from sqlmodel import Session, create_engine, SQLModel

DATABASE_URL = "postgresql://postgres@localhost/netsol"


engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
