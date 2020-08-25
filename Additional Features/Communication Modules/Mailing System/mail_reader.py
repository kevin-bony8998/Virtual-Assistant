import smtplib
import time
import imaplib
import email
import sys
import email_to
from email.header import decode_header
import os

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "nivekynob" + ORG_EMAIL
FROM_PWD    = "Appunni1!"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)

        mail.login(FROM_EMAIL,FROM_PWD)

        mail.select('inbox')


        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]


        id_list = mail_ids.split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])


        for i in range(latest_email_id,first_email_id, -1):
            #print(mail.fetch(i, '(RFC822)' ))

            typ, data = mail.fetch(str(i), '(RFC822)' )

            for response in data:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if it's a bytes, decode to str
                        subject = subject.decode()
                    # email sender
                    from_ = msg.get("From")
                    print("Subject:", subject)
                    print("From:", from_)
                    # if the email message is multipart
                    if msg.is_multipart():
                        # iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                # print text/plain emails and skip attachments
                                print(body)
                            elif "attachment" in content_disposition:
                                # download attachment
                                filename = part.get_filename()
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # print only text email parts
                            print(body)
                    print("="*100)
        imap.close()
        imap.logout()

    except:
        print("Error occured:", sys.exc_info()[0])

read_email()