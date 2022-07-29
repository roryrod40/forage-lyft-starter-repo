from abc import ABC, abstractmethod, abstractclassmethod


class CheckService(ABC):
    @abstractmethod
    def service_needed(self):
        pass
