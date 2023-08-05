#! /usr/local/bin/python
from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
from email.mime.text import MIMEText
try:
    from . import auth
except:
    import auth

def send(**kwargs):
    if('auth' in kwargs):
        params = kwargs['auth']
    else:
        print("Auth not specified. Trying to load auth")
        params = auth.load_default_auth()
    SMTPserver = params['SMTPserver']
    USERNAME = params['USERNAME']
    PASSWORD = params['PASSWORD']
    #fail sender to username if not provided
    if('sender' in params): sender = params['sender']
    else: sender = params['USERNAME']
    text_subtype = 'plain'

    #compose message
    if('destination' in kwargs):
        destination =kwargs['destination']
    elif('to' in kwargs):
        destination = kwargs['to']
    elif('destination' in params):
        print("Trying to load destination from file")
        destination = params['destination']
    elif('to' in params):
        print("Trying to load destination from file")
        destination = params['to']
    else:
        print("No destination specified. Using sender address")
        destination = sender
    if('subject' in kwargs):
        subject=kwargs['subject']
    else:
        subject = "Message from: "+sender
    if('message' in kwargs):
        content=kwargs['message']
    else:
        content = subject
    msg = MIMEText(content, text_subtype)
    msg['Subject']= subject
    msg['From']   = sender # some SMTP servers will do this automatically, not all
    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    except:
        raise Exception("[Error] Unable to send message")
    finally:
        conn.quit()
    return True