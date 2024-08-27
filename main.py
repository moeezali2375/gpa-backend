from fastapi import FastAPI
from .config.databaseConfig import create_db_and_tables
from .routes.authRoutes import router

app = FastAPI()

# ! Include Middlewares
app.include_router(router, prefix="/auth")


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
