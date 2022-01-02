from smtplib import SMTP
from imaplib import IMAP4
from imbox import Imbox

with Imbox('imap.139.com', '13406396981@139.com', 'zxf19751208') as imboxx:
    all_inbox_messages = imboxx.messages()
    for uid, message in all_inbox_messages:
        print(message.subject)
        print(message.body["plain"])
        #       imboxx.delete(uid)
        for attachment in message.attachments:
            print(attachment['filename'])
            with open(attachment['filename'], 'wb') as f:
                f.write(attachment['content'].getvalue())
                f.close()
