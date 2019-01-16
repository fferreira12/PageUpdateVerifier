from subscriber import Subscriber
from data_parser import DataParser
from bs4 import BeautifulSoup


class LastLinkGetter(Subscriber, DataParser):

    def __init__(self, linkSelector):
        self.link_selector = linkSelector
        self.nextHandler: DataParser = None

    def onNewPage(self, page):
        print("Last Link: " + self.getLastLink(page))
    
    def getLastLink(self, page):
        soup = BeautifulSoup(page, 'html.parser')
        last_link = soup.select(self.link_selector)
        last_link_text = last_link[0].contents[0].strip()
        return last_link_text
    
    def getData(self, page, data):
        data["Last_Link"] = self.getLastLink(page)
        return self.goToNextOrReturn(page, data)

    #def setNext(self, nextHandler: DataParser):
    #    self.nextHandler = nextHandler
