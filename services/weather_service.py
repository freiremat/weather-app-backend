import httpx
import os
from dotenv import load_dotenv
from fastapi import HTTPException

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

async def get_weather(city: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={
            "q": city,
            "appid": API_KEY,
            "units": "metric",
            "lang": "pt_br"
        })

#tratamento de erro
    if response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"Cidade '{city}' não encontrada.")
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Erro ao consultar a API de clima.")

    data = response.json()

#retorna da API apenas o necessario
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"],
    }
