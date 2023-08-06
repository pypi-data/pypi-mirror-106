from abc import ABC, abstractmethod


class BaseQueryMarkerStrategy(ABC):
    """"""

    @abstractmethod
    def check(self, x):
        """"""

    @abstractmethod
    def get(self, x):
        """"""
