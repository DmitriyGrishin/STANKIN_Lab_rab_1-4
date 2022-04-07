import email
import imaplib
import os

__all__ = [
    'FetchEmail',
    'DOWNLOAD'
]

SERVER = 'imap.yandex.ru'
DOWNLOAD = 'Download'


class FetchEmail:

    connection = None
    error = None

    def __init__(self, username, password):
        self.connection = imaplib.IMAP4_SSL(SERVER)
        self.connection.login(username, password)
        self.connection.select(readonly=False)  # so we can mark mails as read

    def close_connection(self):
 
        self.connection.close()

    @staticmethod
    def save_attachment(msg, download_folder=os.path.join(os.getcwd(), DOWNLOAD)):
        att_path = "No attachment found."
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            filename = part.get_filename()
            att_path = os.path.join(download_folder, filename)
            os.makedirs(download_folder, exist_ok=True)
            if not os.path.isfile(att_path):
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        return att_path

    def fetch_unread_messages(self):
        emails = []
        (result, messages) = self.connection.search(None, 'UnSeen')
        if result == "OK":
            for message in str(messages[0])[2:-1].split(' '):
                try:
                    ret, data = self.connection.fetch(message, '(RFC822)')
                except:
                    print("No new emails to read.")
                    self.close_connection()
                    exit()

                msg = email.message_from_bytes(data[0][1])
                if not isinstance(msg, str):
                    emails.append(msg)
                response, data = self.connection.store(message, '+FLAGS', '\\Seen')

            return emails

        self.error = "Failed to retreive emails."
        return emails