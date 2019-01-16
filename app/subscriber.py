from abc import ABC, abstractmethod


class Subscriber(ABC):
    """Abstract class that defines a subscriber"""

    @abstractmethod
    def onNewPage(self, page):
        pass
