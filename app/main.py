from typing import Any

from fastapi import FastAPI

from .utils import setup_logging
from .response_models import Root
from .v1.router import router as v1_root_router

setup_logging()
app = FastAPI(
    title="Dune API",
    summary="API for information about Frank Herbert's book series Dune",
    version="0.0.1",
    redoc_url=None,
)


@app.get("/", response_model=Root)
def root() -> Any:
    return {"v1": {"status": "200 OK"}}


app.include_router(v1_root_router, prefix="/v1")