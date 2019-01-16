from abc import ABC, abstractmethod

class Persistence(ABC):
    """Abstract class that defines a persistence unit"""

    @abstractmethod
    def save(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def exists(self, key):
        pass