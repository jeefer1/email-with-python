from email.message import EmailMessage
import smtplib #simple mail transfer protocol
import ssl #secure socket layer or tls-transport layer security
email_sender = "jeefer08@gmail.com"
email_password = "your password"
email_reciver = "linojeefre09@gmail.com"
subject = "lino coconut"
body = "this mail is send by code."
em = EmailMessage()
em["from"] = email_sender
em["to"] = email_reciver
em["subject"] = subject
em.set_content(body)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",465, context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciver,em.as_string())
