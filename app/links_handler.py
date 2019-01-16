import datetime
import json

from subscriber import Subscriber
#from last_link_getter import LastLinkGetter
#from total_links_getter import TotalLinksGetter
from data_parser import DataParser
#from file_persistence import SaveFile, ReadJSON
from persistence import Persistence

class LinksHandler(Subscriber):

    def __init__(self, persistence: Persistence, fileName: str):
        self.persistence = persistence
        self.fileName = fileName
        self.handlers = []
        #self.handlers.append(TotalLinksGetter(listOfLinksSelector))
        #self.handlers.append(LastLinkGetter(lastLinkSelector))
        self.parserChain: DataParser = None
        self.data = {}

    def setParserChain(self, parserChain: DataParser):
        self.parserChain = parserChain

    def onNewPage(self, page):
        #data = ReadJSON(self.fileName)
        data = self.persistence.get(self.fileName)
        # try:
        #     data = json.loads(jsonstr)
        # except:
        #     data = None
        data = data if data is not None else {}
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        data[today] = self.parserChain.getData(page, {})


        # for sub in self.handlers:
        #     data[today].update(sub.getData(page))
        #     sub.onNewPage(page)

        self.persistence.save(self.fileName,data)

