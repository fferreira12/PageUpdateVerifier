from bs4 import BeautifulSoup
import re

from data_parser import DataParser

class LastUpdateHandler(DataParser):

    def __init__(self):
        self.nextHandler: DataParser = None

    def getData(self, page, data):
        soup = BeautifulSoup(page, 'html.parser')
        data['last_update_date'] = re.search(r"\d{2}/\d{2}/\d{4}",soup.find('span', attrs={"class":"ultimaAtualizacao"}).contents[0]).group(0)
        data['last_update_time'] = re.search(r"\d{2}:\d{2}",soup.find('span', attrs={"class":"ultimaAtualizacao"}).contents[0]).group(0)
        return data