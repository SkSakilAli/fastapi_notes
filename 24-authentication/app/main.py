from fastapi import FastAPI
from app.account.models import create_tables
from app.account.routers import router as account_router

app = FastAPI()
app.include_router(account_router)
