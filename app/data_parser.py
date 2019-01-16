from abc import ABC, abstractmethod

class DataParser(ABC):
    """Abstract class that defines a data parser"""

    @abstractmethod
    def getData(self, page, data):
        pass

    @abstractmethod
    def setNext(self, nextHandler):
        pass

    def goToNextOrReturn(self, page, data):
        if self.nextHandler is not None:
            return self.nextHandler.getData(page, data)
        else:
            return data

    def setNext(self, nextHandler: "DataParser"):
        self.nextHandler = nextHandler