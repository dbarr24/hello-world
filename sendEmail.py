import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


email_user = 'stockHawk2018@gmail.com'
email_send = 'stockHawk2018@gmail.com'
subject = 'Python'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
from email import encoders

body = 'Hey it is Pi!'
msg.attach(MIMEText(body,'plain'))

filename = 'BarcodeData.txt'
attachment = open(filename,'rb')

part = MIMEBase('applicaion','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user, 'Cinci123')

server.sendmail(email_user,email_send,text)
server.quit()
