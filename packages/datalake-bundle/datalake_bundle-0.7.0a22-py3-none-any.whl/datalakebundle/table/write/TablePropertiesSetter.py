from logging import Logger
from pyspark.sql.session import SparkSession
from datalakebundle.table.create.TableDefinition import TableDefinition


class TablePropertiesSetter:
    def __init__(self, logger: Logger, spark: SparkSession):
        self.__logger = logger
        self.__spark = spark

    def set(self, table_definition: TableDefinition):
        if table_definition.tbl_properties:
            properties: str = ", ".join([f"'{k}'='{v}'" for k, v in table_definition.tbl_properties.items()])

            self.__logger.info(f"Setting TBLPROPERTIES=({properties})")

            self.__spark.sql(f"ALTER TABLE {table_definition.full_table_name} SET TBLPROPERTIES({properties})")

    def unset(self, table_definition: TableDefinition):
        properties_df = self.__spark.sql(f"SHOW TBLPROPERTIES {table_definition.full_table_name}")
        existing_keys = [
            k
            for k in properties_df.select("key").toPandas()["key"]
            if k not in ["Type", "delta.minReaderVersion", "delta.minWriterVersion"]
        ]

        if existing_keys:
            keys: str = ", ".join([f"'{k}'" for k in existing_keys])

            self.__logger.info(f"Unsetting TBLPROPERTIES=({keys})")

            self.__spark.sql(f"ALTER TABLE {table_definition.full_table_name} UNSET TBLPROPERTIES({keys})")
