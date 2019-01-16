from subscriber import Subscriber
from data_parser import DataParser
from bs4 import BeautifulSoup


class TotalLinksGetter(Subscriber, DataParser):

    def __init__(self, linkSelector):
        self.link_selector = linkSelector
        self.nextHandler: DataParser = None

    def onNewPage(self, page):
        print("Quantity of links: " + str(self.getQuantityOfLinks(page)))

    def getQuantityOfLinks(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        links = soup.select(self.link_selector)
        links = len(links[0].contents)
        return links

    def getData(self, page, data):
        data["Quantity_of_Links"] = self.getQuantityOfLinks(page)
        return self.goToNextOrReturn(page, data)

    #def setNext(self, nextHandler: DataParser):
    #    self.nextHandler = nextHandler
