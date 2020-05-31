# send email via outlook

import smtplib
import os
from email.message import EmailMessage

# set smpt host
try:
    smtpObj = smtplib.SMTP('smtp.office365.com', 587)
except Exception as e:
    print(e)
    smtpObj = smtplib.SMTP_SSL('smtp.office365.com', 465)

#type(smtpObj) 
smtpObj.ehlo()
smtpObj.starttls()

# set login 
User=os.environ['User']
PW=os.environ['PW']

# set email parameters
FROM=os.environ['FROM']
print("Email will be send from: %s" % FROM)

TO=os.environ['TO']
print("Email will be send to: %s" % TO)

Subject = os.environ['Subject']
print("Email subject will be: %s" % Subject)

Body = os.environ['Body']
print("Email body will be: %s" % Body)

Attachment = os.environ['Attachment']
print("Attached file will be: %s" % Attachment)

# Create the container (outer) email message.
msg = EmailMessage()
msg["From"] = FROM
msg["To"] = TO
msg["Subject"] = Subject

msg.set_content(Body)
try:
    msg.add_attachment(open(filename, "r").read(), filename=Attachment)
except:
    print("No Attachment file found")


# login to microsoft account and send email
smtpObj.login(User, PW)
smtpObj.send_message(msg)
print("Successfully sent email")

smtpObj.quit()
