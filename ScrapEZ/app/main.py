from fastapi import FastAPI
from app.routers import scraper

app = FastAPI()

app.include_router(scraper.router)