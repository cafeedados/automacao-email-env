"""
@cafeedados

version: Python 3.10.x
"""
import smtplib 

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

# open html file
f = open('e-mail-file.html', 'r', encoding="UTF-8")
corpo = f.read()

# Adding "teste.txt" file attachment
attachment = open('teste.txt', 'rb')

# Base64 encoding teste.txt file
att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)


host = "smtp.gmail.com"
port = "587"
login = "<email-url>"
password = "<email-pass>"

server = smtplib.SMTP(host, port) # Connect Server

#opening tsl connection
server.ehlo()
server.starttls()

 # Connect to Account
server.login(login, password)

email_msg = MIMEMultipart()

email_msg['From'] =  login
email_msg['To'] = '<email-url>'
email_msg['Subject'] = "My First"
email_msg.attach(MIMEText(corpo, 'html'))

# adding the attachment
att.add_header('Content-Disposition', 'attachment; filename= teste.txt')
attachment.close()
email_msg.attach(att)

# sending email
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
server.quit()