from abc import ABC, abstractmethod

from .basemodel import Model


class UrdfFactory(ABC):
    @abstractmethod
    def build_model(self) -> Model:
        pass
