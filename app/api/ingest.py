from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.db.models import WeatherRecord
from app.core.fetch import fetch_weather
from app.core.transform import transform_weather_data

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ingest/weather")
def ingest_weather(city: str, db: Session = Depends(get_db)):
    raw = fetch_weather(city)
    data = transform_weather_data(raw)

    record = WeatherRecord(**data)
    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "message": "Weather data ingested",
        "city": record.city,
        "temperature": record.temperature
    }
