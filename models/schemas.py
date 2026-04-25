from pydantic import BaseModel

class HistoryItem(BaseModel):
    city: str
    lat: float
    lon: float
    consulted_at: str
