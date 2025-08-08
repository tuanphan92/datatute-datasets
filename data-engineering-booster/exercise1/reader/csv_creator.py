from reader.base_creator import Creator
from reader.base_reader import DataReader
from reader.csv_reader import CSVReader
from reader.csv_reader import CSVConfig


class CSVCreator(Creator):
    """
    Concrete Creator for reading from CSV files.
    """

    def __init__(self, config: CSVConfig) -> None:
        super().__init__(config)

    def get_data_reader(self) -> DataReader:
        return CSVReader(self.config)
