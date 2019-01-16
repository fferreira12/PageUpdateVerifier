import sys
import hashlib

from subscriber import Subscriber
from publisher import Publisher
#from file_persistence import FileExists, ReadFile, SaveFile
from persistence import Persistence

class FileComparer(Subscriber, Publisher):
    """FileComparer is both a publisher and a subscriber"""

    def __init__(self, persistence: Persistence, fileName):
        self.file_name = fileName
        self.current_page = ""
        self.subscribers = []
        self.persistence = persistence
        if(self.persistence.exists(fileName)):
            print("Page already exists. Getting Page")
            self.current_page = self.persistence.get(fileName)
            self.current_hash = self.hash(self.current_page)
            #print("First Line of File: ")
            #print(self.current_page.split('\n', 1)[0])

    def onNewPage(self, page):
        actual_hash = self.persistence.get(self.file_name)
        new_hash = self.hash(page)
        print("Current page hash: " + actual_hash)
        print("New page hash: " + new_hash)
        
        if(new_hash == actual_hash):
            print("Pages are equal")
        else:
            print("Pages are different. Check website")
            self.persistence.save(self.file_name, new_hash)
            
            #emit in case of new page
            self.emit(page)
            
            #sys.exit(0)

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def emit(self, data):
        for sub in self.subscribers:
            sub.onNewPage(data)

    def hash(self, string):
        return hashlib.md5(string.encode()).hexdigest()