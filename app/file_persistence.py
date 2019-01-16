import os
import json
import codecs

from persistence import Persistence

class FilePersistence(Persistence):

    @staticmethod
    def SaveFile(fileName, file):
        """Saves a file to disk"""
        f = open(fileName,"w+")
        if(isinstance(file,dict)):
            file = FilePersistence.ConvertToString(file)
        f.write(file)

    @staticmethod
    def ReadFile(fileName):
        """Reads a file from disk"""
        if(FilePersistence.FileExists(fileName)):
            return open(fileName, "r").read()
        else:
            return None

    @staticmethod
    def ReadJSON(fileName):
        if(FilePersistence.FileExists(fileName)):
            return json.loads(FilePersistence.ReadFile(fileName))
        else:
            return None

    @staticmethod
    def FileExists(fileName):
        """Checks if a file exists"""
        try:
            st = os.stat(fileName)
        except os.error:
            return False
        return True

    @staticmethod
    def ConvertToString(dict):
        #s = json.dumps(dict, ensure_ascii=False)
        #data = json.dumps(dict, ensure_ascii=False)
        return json.dumps(dict, ensure_ascii=False)

    def save(self, key, value):
        return FilePersistence.SaveFile(key, value)

    def get(self, key):
        return FilePersistence.ReadFile(key)

    def exists(self, key):
        return FilePersistence.FileExists(key)