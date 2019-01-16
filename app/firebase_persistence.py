import sys
import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from persistence import Persistence


class FirebasePersistence(Persistence):

    def __init__(self):

        #self.cred = credentials.Certificate(r'C:\Users\fferr\Google Drive\Contests\Scripts\app\firebase-credentials.json')
        #self.cred = credentials.Certificate(r'/home/ubuntu/page-update-verifier/firebase-credentials.json')
        self.cred = credentials.Certificate(os.path.join(sys.path[0], "firebase-credentials.json"))

        firebase_admin.initialize_app(self.cred, {'databaseURL': 'https://page-update-verifier-1799e.firebaseio.com'})
        self.ref = db.reference('verifications')

    def save(self, key, value):
        if(value is not None and value != {}):
            self.ref.update({key: value})

    def get(self, key):
        data = self.ref.get()
        try:
            t = data[key]
        except KeyError:
            t = None
        return t

    def exists(self, key):
        data = self.ref.get()
        try:
            t = data[key]
        except KeyError:
            t = None
        return t is not None


if __name__ == "__main__":
    firebasePersistence = FirebasePersistence()
    firebasePersistence.save("D", "FERNANDO RODRIGUES")
    firebasePersistence.get("currentpage")