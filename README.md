# Minimal Docker Image to send Outlook emails with Python

This image contains a Python 3 script for sending emails from Outlook with Python library `email` (https://docs.python.org/3/library/email.html). For sending automated emails SMTP has to be activated in your Outlook IMAP and POP settings. The Docker container takes the following environment variables as specified in the docker-compose.yml:

      - User= Outlook account mail address
      - PW= Outlook account password
      - FROM= Sender mail address
      - TO= Reciever mail address
      - Subject= Mail Subject 
      - Body= Mail body
      - Attachment= attachments to send


The Docker Image can be pulled from Docker Hub via `docker pull timosch29/send_email_python`.
