from greyai_sdk.dataset import Dataset, DatasetType
from pydantic import BaseModel
from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self, strategy=None, model_file=None):
        self.model = None
        self.model_file = model_file
        self.strategy = strategy

    @abstractmethod
    def predict(self, datasets: Dataset) -> BaseModel:
        pass

    @abstractmethod
    def train(self, datasets: Dataset) -> str:
        pass

    @abstractmethod
    def customizable(self) -> bool:
        pass

    @abstractmethod
    def accepts_input(self) -> DatasetType:
        pass

