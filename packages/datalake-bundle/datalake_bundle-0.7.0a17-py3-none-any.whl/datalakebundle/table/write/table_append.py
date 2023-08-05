from typing import Union
from daipecore.decorator.DecoratedDecorator import DecoratedDecorator
from daipecore.decorator.OutputDecorator import OutputDecorator
from injecta.container.ContainerInterface import ContainerInterface
from pyspark.sql import DataFrame
from datalakebundle.table.create.TableDefinitionFactory import TableDefinitionFactory
from datalakebundle.table.schema.TableSchema import TableSchema
from datalakebundle.table.write.TableAppender import TableAppender


@DecoratedDecorator
class table_append(OutputDecorator):  # noqa: N801
    def __init__(self, table_identifier_or_schema: Union[str, TableSchema], options: dict = None):
        self.__table_identifier_or_schema = table_identifier_or_schema
        self.__options = options or {}

    def process_result(self, result: DataFrame, container: ContainerInterface):
        table_definition_factory: TableDefinitionFactory = container.get(TableDefinitionFactory)
        table_appender: TableAppender = container.get(TableAppender)

        if isinstance(self.__table_identifier_or_schema, str):
            table_definition = table_definition_factory.create_from_dataframe(
                self.__table_identifier_or_schema, result, self.__class__.__name__
            )
        elif isinstance(self.__table_identifier_or_schema, TableSchema):
            table_definition = table_definition_factory.create_from_table_schema(self.__table_identifier_or_schema)
        else:
            raise Exception(f"Invalid table identifier: {self.__table_identifier_or_schema}")

        table_appender.append(result, table_definition, self.__options)
