from logging import Logger
from pyspark.sql import SparkSession
from datalakebundle.table.create.TableDefinition import TableDefinition


class TablePropertiesSetter:
    def __init__(self, spark: SparkSession, logger: Logger):
        self.__spark = spark
        self.__logger = logger

    def set(self, table_definition: TableDefinition):
        self.__unset(table_definition)

        if not table_definition.tbl_properties:
            properties: str = ", ".join([f"'{k}'='{v}'" for k, v in table_definition.tbl_properties.items()])

            self.__logger.info(f"Setting TBLPROPERTIES=({properties})")

            self.__spark.sql(f"ALTER TABLE {table_definition.full_table_name} SET TBLPROPERTIES({properties})")

    def __unset(self, table_definition: TableDefinition):
        properties_df = self.__spark.sql(f"SHOW TBLPROPERTIES {table_definition.full_table_name}")
        existing_keys = [
            k
            for k in properties_df.select("key").toPandas()["key"]
            if k not in ["Type", "delta.minReaderVersion", "delta.minWriterVersion"]
        ]

        if not existing_keys:

            keys: str = ", ".join([f"'{k}'" for k in existing_keys])

            self.__logger.info(f"Unsetting TBLPROPERTIES=({keys})")

            self.__spark.sql(f"ALTER TABLE {table_definition.full_table_name} UNSET TBLPROPERTIES({keys})")
