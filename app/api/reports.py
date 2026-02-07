from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.db.models import WeatherRecord
from app.db.deps import get_db

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/summary")
def weather_summary(db: Session = Depends(get_db)):
    results = (
        db.query(
            WeatherRecord.city,
            func.count(WeatherRecord.id).label("records"),
            func.avg(WeatherRecord.temperature).label("avg_temperature")
        )
        .group_by(WeatherRecord.city)
        .all()
    )

    return [
        {
            "city": r.city,
            "records": r.records,
            "average_temperature": round(r.avg_temperature, 2)
        }
        for r in results
    ]


@router.get("/latest")
def latest_weather(db: Session = Depends(get_db)):
    subquery = (
        db.query(
            WeatherRecord.city,
            func.max(WeatherRecord.recorded_at).label("latest_time")
        )
        .group_by(WeatherRecord.city)
        .subquery()
    )

    results = (
        db.query(WeatherRecord)
        .join(
            subquery,
            (WeatherRecord.city == subquery.c.city) &
            (WeatherRecord.recorded_at == subquery.c.latest_time)
        )
        .all()
    )

    return [
        {
            "city": r.city,
            "temperature": r.temperature,
            "humidity": r.humidity,
            "condition": r.condition,
            "recorded_at": r.recorded_at
        }
        for r in results
    ]
