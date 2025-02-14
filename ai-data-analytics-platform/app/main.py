from fastapi import FastAPI
from app.api import ingest

app = FastAPI()

app.include_router(ingest.router, prefix="/data", tags=["Data Ingestion"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Data Analytics Platform"}