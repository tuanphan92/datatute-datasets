from reader.base_reader import DataReader
import pandas as pd
from typing import TypedDict, Optional


class CSVConfig(TypedDict):
    file_path: str
    sep: Optional[str] = ","  # separator, e.g., ',', '\t', '|'
    encoding: Optional[str] = "utf-8"


class CSVReader(DataReader):
    """
    Concrete Product for reading CSV files.
    """

    def __init__(self, config: CSVConfig) -> None:
        self.config = config

    def read_data(self) -> pd.DataFrame:
        return pd.read_csv(
            self.config["file_path"],
            sep=self.config.get("sep", ","),
            encoding=self.config.get("encoding", "utf-8"),
        )
