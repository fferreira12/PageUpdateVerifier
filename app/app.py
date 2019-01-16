import time

from page_downloader import PageDownloader
from checks_counter import ChecksCounter
from file_comparer import FileComparer
#from last_link_getter import LastLinkGetter
#from total_links_getter import TotalLinksGetter
from links_handler import LinksHandler
from email_handler import EmailHandler
from last_link_getter import LastLinkGetter
from total_links_getter import TotalLinksGetter
from last_update_handler import LastUpdateHandler
#from file_persistence import FilePersistence
from firebase_persistence import FirebasePersistence
from config import Config

downloader = PageDownloader("http://www.concursosfcc.com.br/concursos/caldf118/index.html")
#config = Config("/home/ubuntu/page-update-verifier/config.json")
config = Config("config.json")

#filePersistence = FilePersistence()
firebasePersistence = FirebasePersistence()

numberChecker = ChecksCounter(firebasePersistence, config["verifications_save"])
fileComparer = FileComparer(firebasePersistence, config["page_save"])
linksHandler = LinksHandler(firebasePersistence, config["data_save"])

parser1 = LastLinkGetter(config["last_link_selector"])
parser2 = TotalLinksGetter(config["links_selector"])
parser3 = LastUpdateHandler()
parser1.setNext(parser2)
parser2.setNext(parser3)

linksHandler.setParserChain(parser1)

emailHandler = EmailHandler(config["email_from"], config["password"], config["email_to"])

secondsBetween = config["time_interval"]

downloader.subscribe(numberChecker)
downloader.subscribe(linksHandler)
downloader.subscribe(fileComparer)
fileComparer.subscribe(emailHandler)

# Do continuously
# while(True):
#    downloader.downloadPage()
#    print("------------------------------")
#    time.sleep(secondsBetween)

##Do Once
downloader.downloadPage()