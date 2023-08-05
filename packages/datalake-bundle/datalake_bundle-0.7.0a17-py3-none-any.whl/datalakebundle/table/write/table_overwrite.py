from typing import Union
from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from daipecore.decorator.OutputDecorator import OutputDecorator
from injecta.container.ContainerInterface import ContainerInterface
from pyspark.sql import DataFrame
from datalakebundle.table.create.TableDefinitionFactory import TableDefinitionFactory
from datalakebundle.table.schema.TableSchema import TableSchema
from datalakebundle.table.write.TableOverwriter import TableOverwriter


@DecoratedDecorator
class table_overwrite(OutputDecorator):  # noqa: N801
    def __init__(self, table_identifier_or_schema: Union[str, TableSchema], recreate_table: bool = False, options: dict = None):
        self.__table_identifier_or_schema = table_identifier_or_schema
        self.__recreate_table = recreate_table
        self.__options = options or {}

    def process_result(self, result: DataFrame, container: ContainerInterface):
        table_definition_factory: TableDefinitionFactory = container.get(TableDefinitionFactory)
        table_overwriter: TableOverwriter = container.get(TableOverwriter)

        if isinstance(self.__table_identifier_or_schema, str):
            table_definition = table_definition_factory.create_from_dataframe(
                self.__table_identifier_or_schema, result, self.__class__.__name__
            )
        elif isinstance(self.__table_identifier_or_schema, TableSchema):
            table_definition = table_definition_factory.create_from_table_schema(self.__table_identifier_or_schema)
        else:
            raise Exception(f"Invalid table identifier: {self.__table_identifier_or_schema}")

        table_overwriter.overwrite(result, table_definition, self.__recreate_table, self.__options)
