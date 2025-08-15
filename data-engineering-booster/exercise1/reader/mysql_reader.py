from reader.base_reader import DataReader
import pandas as pd
import urllib
from typing import TypedDict

from sqlalchemy import create_engine, Engine


class MySQLConfig(TypedDict):
    server: str
    database: str
    username: str
    password: str
    query: str


class MySQLReader(DataReader):
    """
    Concrete Product for reading MySQL database.
    """

    def __init__(self, config: MySQLConfig) -> Engine:
        self.config = config

    def get_connection(self) -> None:
        # Use the format for the PyMySQL driver.
        password = urllib.parse.quote_plus(self.config["password"])
        connection_uri = (
            f"mysql+pymysql://{self.config['username']}:{password}"
            f"@{self.config['server']}:3306/{self.config['database']}"
        )
        engine = create_engine(connection_uri)
        return engine

    def read_data(self) -> pd.DataFrame:
        return pd.read_sql(sql=self.config["query"], con=self.get_connection())
