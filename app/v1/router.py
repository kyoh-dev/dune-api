from logging import getLogger
from sqlite3 import Connection
from typing import Any, Annotated

from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import RedirectResponse

from .dependencies import get_db_connection, CommonQueryParams
from .queries import (
    read_characters,
    read_random_character,
    read_houses,
    read_organisations,
)
from .response_models import PaginatedResponse
from ..utils import paginated_response

logger = getLogger(__name__)
router = APIRouter()


@router.get("/", response_class=RedirectResponse)
async def root() -> Any:
    return RedirectResponse(url="/docs")


@router.get("/characters", response_model=PaginatedResponse)
def get_characters(
    common_query_params: CommonQueryParams,
    house: Annotated[
        str | None, Query(strict=True, examples=["Atreides", "atreides"])
    ] = None,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    characters = read_characters(
        db_conn, house, common_query_params["limit"], common_query_params["offset"]
    )

    if not characters and house is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, House {house.capitalize()} does not exist",
        )

    return paginated_response(
        characters, common_query_params["limit"], common_query_params["offset"]
    )


@router.get("/character/random", response_model=PaginatedResponse)
def get_random_character(db_conn: Connection = Depends(get_db_connection)) -> Any:
    character = read_random_character(db_conn)

    if not character:
        logger.error("Could not get a random character from database")
        raise HTTPException(status_code=500, detail="No data available")

    return paginated_response([character], 0, 0)


@router.get("/houses", response_model=PaginatedResponse)
def get_houses(
    common_query_params: CommonQueryParams,
    status: Annotated[
        str | None, Query(strict=True, examples=["Major", "major"])
    ] = None,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    houses = read_houses(
        db_conn, status, common_query_params["limit"], common_query_params["offset"]
    )

    if not houses and status is not None:
        raise HTTPException(
            status_code=404,
            detail=f"Items not found, status House {status.capitalize()} does not exist",
        )

    return paginated_response(
        houses, common_query_params["limit"], common_query_params["offset"]
    )


@router.get("/organisations", response_model=PaginatedResponse)
def get_organisations(
    common_query_params: CommonQueryParams,
    db_conn: Connection = Depends(get_db_connection),
) -> Any:
    organisations = read_organisations(
        db_conn, common_query_params["limit"], common_query_params["offset"]
    )

    if not organisations:
        raise HTTPException(status_code=404, detail="Items not found")

    return paginated_response(
        organisations, common_query_params["limit"], common_query_params["offset"]
    )
