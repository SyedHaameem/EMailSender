from email.message import EmailMessage
import ssl
import smtplib
from emil import emaill

sender="therehere876@gmail.com"
password="kgnhfxsfqxnlunhk"
reciver=emaill

subject="HELLO HAAMEEM"

body="""

HELLO BUDDY ,HOW ARE DOING TODAY

"""

EM=EmailMessage()
EM['From']=sender
EM['to']=reciver
EM["subject"]=subject
EM.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('ssl,gmail.com',465,context=context) as smtp:
    smtp.login(sender,password)
    smtp.sendmail(sender,reciver,EM.as_string())