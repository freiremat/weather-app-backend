from fastapi.testclient import TestClient
from fastapi import HTTPException
from unittest.mock import patch, AsyncMock
from main import app

client = TestClient(app)

MOCK_WEATHER = {
    "city": "London",
    "temp": 15.0,
    "feels_like": 13.0,
    "humidity": 72,
    "wind_speed": 4.5,
    "description": "nublado",
    "lat": 51.5074,
    "lon": -0.1278,
}

def test_weather_cidade_valida():
    with patch("routes.weather.get_weather", new=AsyncMock(return_value=MOCK_WEATHER)):
        response = client.get("/api/weather?city=London")

    assert response.status_code == 200

    data = response.json()

    assert "temp" in data
    assert data["city"] == "London"

def test_weather_cidade_sem_parametro():
    response = client.get("/api/weather") 

    assert response.status_code != 200

def test_weather_cidade_inexistente():
    with patch("routes.weather.get_weather", new=AsyncMock(side_effect=HTTPException(
        status_code=404, detail="Cidade 'cidadeInexistente' não encontrada."))):
        response = client.get("/api/weather?city=cidadeInexistente")

    assert response.status_code == 404
    assert "não encontrada" in response.json()["detail"]
