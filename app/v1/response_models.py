from datetime import datetime

from pydantic import BaseModel, ConfigDict, Json


class CustomBase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    created_at: datetime
    updated_at: datetime


class Character(CustomBase):
    # TODO: add aliases
    titles: Json[list[str]] | None
    first_name: str
    last_name: str | None
    suffix: str | None
    dob: str
    birthplace: str
    dod: str | None
    house: str | None
    organisation: str | None


class House(CustomBase):
    name: str
    homeworld: Json[list[str]]
    status: str
    colours: Json[list[str]]
    symbol: str


class Organisation(CustomBase):
    name: str
    founded: str
    dissolved: str | None
