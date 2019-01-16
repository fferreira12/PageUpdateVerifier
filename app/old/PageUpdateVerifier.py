from urllib.request import urlopen
import urllib
import time
import os
import datetime
from bs4 import BeautifulSoup

def DownloadPage(url):
    html = ""
    try:
        html = urlopen(url)
    except urllib.error.URLError:
        print("Could not fetch the page")
    return html

def DecodePage(response):
    html_response = response.read()
    encoding = response.headers.get_content_charset('utf-8')
    decoded_html = html_response.decode(encoding)
    return decoded_html

def SaveFile(fileName, file):
    f = open(fileName,"w+")
    f.write(file)

def HasChanged(oldPage, newPage):
    return oldPage != newPage

def HasActualPage(fileName):
    """Test whether a path exists.  Returns False for broken symbolic links"""
    try:
        st = os.stat(fileName)
    except os.error:
        return False
    return True

def Run(fileName, url, secondsBetween):
    if(not HasActualPage(fileName)):
        print("Getting page for first time")
        SaveFile(fileName, DecodePage(DownloadPage(url)))
    i = GetVerificationNumber()
    while(True):
        i = i + 1
        SaveVerificationNumber(i)
        print("Awaiting next Verification. " + str(i) + " Tests made")
        time.sleep(secondsBetween)
        oldFile = open(fileName, "r").read()
        newFile = (DownloadPage(url))
        if(newFile != ""):
            newFile = DecodePage(newFile)
            print("Last link: " + GetLastLink(newFile))
            if(oldFile != newFile):
                print("Files are different. Check website for news.")
                print("Saving new file to disk")
                SaveFile(fileName, newFile)
                print("File saved at " + str(datetime.datetime.now()).split('.')[0])
                break
        else:
            print("Retrying to get page")
    SaveVerificationNumber(i)

def GetLastLink(document):
    soup = BeautifulSoup(document, 'html.parser')
    last_link = soup.select("#centro2 > div.linkArquivo > div:nth-of-type(1) > a > div.linkArquivoTexto")
    return last_link[0].contents[0].strip()

def SaveVerificationNumber(number):
    SaveFile("verifications.txt", str(number))
    
def GetVerificationNumber():
    return int(open("verifications.txt", "r").read())

fileName = "currentpage.html"
url = "http://www.concursosfcc.com.br/concursos/caldf118/index.html"
interval = 60

Run(fileName, url, interval)