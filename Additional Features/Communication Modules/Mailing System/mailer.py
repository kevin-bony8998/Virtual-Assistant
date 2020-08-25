

import smtplib
import time
import imaplib
import email
import sys
import email_to

server = email_to.EmailServer('smtp.gmail.com', 587, 'poject.hades.storage@gmail.com', 'Appunni3#')
server.quick_email('kevin_bony@yahoo.com', 'Test',
                   ['# A Heading', 'Something else in the body'],
                   style='h1 {color: blue}')