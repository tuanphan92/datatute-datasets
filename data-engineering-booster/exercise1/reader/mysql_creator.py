from reader.base_creator import Creator
from reader.base_reader import DataReader
from reader.mysql_reader import MySQLReader
from reader.mysql_reader import MySQLConfig


class MySQLCreator(Creator):
    """
    Concrete Creator for reading from MySQL database.
    """

    def __init__(self, config: MySQLConfig) -> None:
        super().__init__(config)

    def get_data_reader(self) -> DataReader:
        return MySQLReader(self.config)
