from abc import ABC, abstractmethod


class ActionHandler(ABC):

    @abstractmethod
    def execute(self):
        pass