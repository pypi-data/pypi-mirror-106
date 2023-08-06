from abc import ABC, abstractmethod


class BaseMapping(ABC):
    """"""
    
    @abstractmethod
    def create_map(self, query_paths):
        """"""
