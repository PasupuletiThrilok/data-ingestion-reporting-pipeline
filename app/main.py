from fastapi import FastAPI
from app.db.database import engine
from app.db import models
from app.api.ingest import router as ingest_router
from app.api.reports import router as reports_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(ingest_router)
app.include_router(reports_router)

@app.get("/")
def health_check():
    return {"status": "ok"}
