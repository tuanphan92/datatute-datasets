from abc import ABC, abstractmethod
from reader.base_reader import DataReader
import pandas as pd
import re


class Creator(ABC):
    """
    Abstract Creator class.
    This declares the factory method that returns an object of a Product class (data reader class)
    The Creator's subclasses provide the implementation of this method
    """

    @abstractmethod
    def get_data_reader(self) -> DataReader:
        """
        Method to get the DataReader object
        """

        pass

    def read_data(self) -> pd.DataFrame:
        """
        Method to use the DataReader object to read source data into Pandas dataframe then conform column names to snake case
        """

        data_reader = self.get_data_reader()
        df = data_reader.read_data()
        df = self.to_snake_case(df)
        return df

    def to_snake_case(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Method to rename columns in the source data to snake_case.
        Handles:
        - CamelCase ("ColumnName" -> "column_name")
        - Normal writing format with spaces ("Column name" -> "column_name")
        - Hyphenated names ("Column-Name" -> "column_name")
        """
        new_df = df.copy(deep=True)

        # Replace spaces with underscores first (handles normal writing format)
        new_df.columns = [col.replace(" ", "_") for col in new_df.columns]

        # Regex to convert camel case to snake case
        regex = r"(?<!^)(?=[A-Z])"
        new_df.columns = [
            re.sub(regex, "_", col)  # insert underscore before capitals
            .replace("-", "_")  # replace hyphens with underscores
            .lower()  # lowercase everything
            for col in new_df.columns
        ]

        # Handle cases with multiple underscores (e.g., "Column Name-Test" -> "column__name_test")
        new_df.columns = [re.sub(r"_+", "_", col).strip("_") for col in new_df.columns]
        return new_df
