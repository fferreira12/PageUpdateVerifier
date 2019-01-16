import smtplib

from subscriber import Subscriber

class EmailHandler(Subscriber):
    
    def __init__(self, username, password, toEmail):
        self.username = username
        self.password = password
        self.toEmail = toEmail

    def onNewPage(self, page):
        self.sendEmail()

    def sendEmail(self):
        msg = 'Subject: {}\n\n{}'.format("Page Verifier News", "Page has changed. Check the website")
        print("Sending email")
        s = smtplib.SMTP("smtp.gmail.com",587)
        s.starttls()
        s.ehlo()
        try:
            s.login(self.username, self.password)
            s.sendmail(self.username, self.toEmail, msg)
            print("Email sent")
        except:
            print ('SMTPAuthenticationError')
        s.quit()
        