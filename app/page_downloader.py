from urllib.request import urlopen
import urllib

from publisher import Publisher

class PageDownloader(Publisher):

    def __init__(self, url):
        self.url = url
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def downloadPage(self):
        html = ""
        page = ""
        try:
            html = urlopen(self.url)
            page = self.decodePage(html)
            self.emit(page)
        except urllib.error.URLError:
            print("Could not fetch the page")
        return page
    
    def decodePage(self, response):
        html_response = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        decoded_html = html_response.decode(encoding)
        return decoded_html

    def emit(self, data):
        for sub in self.subscribers:
            sub.onNewPage(data)