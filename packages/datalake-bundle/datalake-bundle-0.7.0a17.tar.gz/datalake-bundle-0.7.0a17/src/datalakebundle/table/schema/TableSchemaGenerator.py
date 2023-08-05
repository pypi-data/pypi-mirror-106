from pyspark.sql import DataFrame


class TableSchemaGenerator:
    def generate(self, table_identifier: str, df: DataFrame) -> str:
        table_schema = ""

        table_schema += "table_schema = TableSchema(\n"
        table_schema += f'    "{table_identifier}",\n'
        table_schema += "    [\n"

        for field in df.schema:
            table_schema += f'        t.StructField("{field.name}", t.{field.dataType}()),\n'

        table_schema += "    ],\n"
        table_schema += '    #  primary_key="",  # INSERT PRIMARY KEY COLUMN(s) HERE (OPTIONAL)\n'
        table_schema += '    #  partition_by="",  # INSERT PARTITION KEY COLUMN(s) HERE (OPTIONAL)\n'
        table_schema += ")\n"

        return table_schema
