from sqlite3 import DatabaseError, Cursor, connect
from typing import Any

from app.v1.constants import DB_PATH


class DbClient:
    def __init__(self, file_path: str, mode: str = "ro") -> None:
        self.file_path = file_path
        self.mode = mode

        try:
            self.conn = connect(
                f"file:{self.file_path}?mode={self.mode}",
                uri=True,
                isolation_level=None,
            )
            self.conn.row_factory = self.dict_row_factory
        except DatabaseError as ex:
            raise RuntimeError("Fatal: Unable to connect to database") from ex

    @staticmethod
    def dict_row_factory(cursor: Cursor, row: tuple[Any, ...]) -> dict[str, Any]:
        fields = [column[0] for column in cursor.description]
        return {k: v for k, v in zip(fields, row)}


db_client = DbClient(DB_PATH)
