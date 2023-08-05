from typing import Union
from pyspark.sql.types import StructType


class TableSchema(StructType):
    def __init__(
        self, full_table_identifier: str, fields: list, primary_key: Union[str, list] = None, partition_by: Union[str, list] = None,
            tbl_properties: dict = None
    ):
        primary_key = primary_key or []
        partition_by = partition_by or []
        tbl_properties = tbl_properties or {}

        if not isinstance(primary_key, str) and not isinstance(primary_key, list):
            raise Exception(f"Invalid primary key: {primary_key}")

        if not isinstance(partition_by, str) and not isinstance(partition_by, list):
            raise Exception(f"Invalid partition by: {partition_by}")

        if not isinstance(tbl_properties, dict):
            raise Exception(f"Invalid tbl_properties by: {tbl_properties}")

        super().__init__(fields)

        full_table_identifier_split = full_table_identifier.split(".")

        self.__db_identifier = full_table_identifier_split[0]
        self.__table_identifier = full_table_identifier_split[1]
        self.__primary_key = [primary_key] if isinstance(primary_key, str) else primary_key
        self.__partition_by = [partition_by] if isinstance(partition_by, str) else partition_by
        self.__tbl_properties = tbl_properties

    @property
    def table_identifier(self):
        return self.__table_identifier

    @property
    def db_identifier(self):
        return self.__db_identifier

    @property
    def full_table_identifier(self):
        return self.__db_identifier + "." + self.__table_identifier

    @property
    def primary_key(self) -> list:
        return self.__primary_key

    @property
    def partition_by(self) -> list:
        return self.__partition_by

    @property
    def tbl_properties(self) -> dict:
        return self.__tbl_properties
