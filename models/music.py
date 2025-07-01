from pydantic import BaseModel
from typing import Optional

class Music(BaseModel):
    music_id: str
    title: str
    artists: list[str]
    genres: list[str]
    spotify: str
    audio: str
    image: Optional[str] = None
    video: Optional[str] = None