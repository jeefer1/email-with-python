import smtplib
server = smtplib.SMTP("smtp.gmail.com",587) #portnumber 587 or 465
server.starttls() #server connection with security
server.login("jeefer08@gmail.com","your password")
server.sendmail("jeefer08@gmail.com","linojeefre09@gmail.com","hello")
print("send mail")
