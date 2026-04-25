from fastapi import APIRouter, Query, HTTPException
from services.weather_service import get_weather
from models.schemas import HistoryItem
from datetime import datetime

router = APIRouter()

history: list[HistoryItem] = []

@router.get("/weather")
async def weather(city: str = Query(..., description="Nome da cidade")):
    data = await get_weather(city)
    history.append(HistoryItem(
        city=data["city"],
        lat=data["lat"],
        lon=data["lon"],
        consulted_at=datetime.now().isoformat()
    ))
    return data

@router.get("/history")
def get_history():
    return history
