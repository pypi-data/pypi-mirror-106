from abc import ABC, abstractmethod


class BasePostProcessor(ABC):
    """"""
    
    @abstractmethod
    def process(self, x):
        """"""
