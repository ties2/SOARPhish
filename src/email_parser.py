import email
from email import policy
from email.parser import BytesParser

class EmailParser:
    def __init__(self, email_file):
        self.email_file = email_file

    def parse_email(self):
        with open(self.email_file, 'rb') as f:
            msg = BytesParser(policy=policy.default).parse(f)

        email_details = {
            'subject': msg['subject'],
            'from': msg['from'],
            'to': msg['to'],
            'date': msg['date'],
            'body': self._get_email_body(msg),
            'attachments': self._get_attachments(msg),
            'links': self._extract_links(self._get_email_body(msg))
        }
        return email_details

    def _get_email_body(self, msg):
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    return part.get_payload(decode=True).decode()
        else:
            return msg.get_payload(decode=True).decode()

    def _get_attachments(self, msg):
        attachments = []
        for part in msg.walk():
            if part.get_filename():
                attachments.append(part.get_filename())
        return attachments

    def _extract_links(self, text):
        import re
        url_pattern = re.compile(r'https?://[^\s]+')
        return url_pattern.findall(text)