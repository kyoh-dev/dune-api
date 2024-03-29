from datetime import datetime

from pydantic import BaseModel, Json

from ..response_models import CustomBase


class Character(CustomBase):
    titles: Json[list[str]] | None
    aliases: Json[list[str]] | None
    first_name: str
    last_name: str | None
    suffix: str | None
    dob: str
    birthplace: str
    dod: str | None
    house: str | None
    organisation: str | None
    created_at: datetime
    updated_at: datetime


class House(CustomBase):
    name: str
    homeworld: Json[list[str]]
    status: str
    colours: Json[list[str]]
    symbol: str
    created_at: datetime
    updated_at: datetime


class Organisation(CustomBase):
    name: str
    founded: str
    dissolved: str | None
    created_at: datetime
    updated_at: datetime


class PaginatedResponse(BaseModel):
    items: list[Character | House | Organisation]
    limit: int
    offset: int
    total: int
