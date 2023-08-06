from abc import ABC, abstractmethod


class BasePathInterpreter(ABC):
    """"""

    @abstractmethod
    def interpret(self, expression):
        """"""
