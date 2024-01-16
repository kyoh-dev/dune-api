from collections.abc import Generator
from sqlite3 import Connection

from app.v1.database import db_client


def get_db_connection() -> Generator[Connection, None, None]:
    try:
        with db_client.conn as conn:
            yield conn
    finally:
        db_client.conn.close()
