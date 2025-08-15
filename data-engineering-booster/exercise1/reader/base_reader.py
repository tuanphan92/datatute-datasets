import numpy as np
import pandas as pd
from abc import ABC, abstractmethod


class DataReader(ABC):
    """
    Abstract base class for data readers.
    In a factory pattern, this acts as the Product interface for operations that all concrete readers must implement
    """

    @abstractmethod
    def read_data(self) -> pd.DataFrame:
        pass
