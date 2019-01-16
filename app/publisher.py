from abc import ABC, abstractmethod

class Publisher(ABC):
    """Abstract class that defines a publisher"""

    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def emit(self, data):
        pass
