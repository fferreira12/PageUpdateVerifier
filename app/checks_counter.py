from subscriber import Subscriber
#from file_persistence import FileExists, ReadFile, SaveFile
from persistence import Persistence

class ChecksCounter(Subscriber):
    """Keeps track of how many checks were made."""
    
    def __init__(self, persistence: Persistence, fileName: str):
        self.current_value = 0
        self.file_name = fileName
        self.persistence = persistence
        if(self.persistence.exists(fileName)):
            self.current_value = int(self.persistence.get(fileName))

    def onNewPage(self, page):
        self.current_value += 1
        print(str(self.current_value) + " checks made")
        self.persistence.save(self.file_name, str(self.current_value))