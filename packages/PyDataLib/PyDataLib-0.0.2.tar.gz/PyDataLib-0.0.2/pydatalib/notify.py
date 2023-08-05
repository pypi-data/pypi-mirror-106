import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.utils import COMMASPACE, formatdate

class Notification:
    def __init__(self, usr, pwd):
        self.__usr = usr
        self.__pwd = pwd
    def sendMail(self, to, subject, body):
        smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
        smtp_ssl_port = 465
        
        msg = MIMEMultipart()
        msg['Date'] = formatdate(localtime=True)
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'html')) # 'plain'
        with smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port) as server:
            server.login(self.__usr, self.__pwd)
            server.sendmail('', to, msg.as_string())