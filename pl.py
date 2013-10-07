import quopri
import html.parser
import mailbox
import re

def get_email_body(email_message):
    def toutf(part):
        charset = part.get_content_charset() if part.get_content_charset() is not None else 'utf-8'
        s = part.get_payload(decode=True)
        if part.get_content_type() == "text/html":
            h = html.parser.HTMLParser()
            return h.unescape(str(s, charset))
        else:
            return str(quopri.decodestring(s), charset)
    maintype = email_message.get_content_maintype()
    if maintype == 'multipart':
        for part in email_message.get_payload():
            if part.get_content_maintype() == 'text':
                return toutf(part)
            elif maintype == 'text':
                return toutf(email_message)
    else:
        return toutf(email_message)

regex = re.compile(r'.*(?P<direction>long|shorted) (?P<instrument>[A-Za-z/]*) @ (?P<entry>[0-9]*[.,]?[0-9]+).*protective stop @ (?P<stop>[0-9]*[.,]?[0-9]+)')

def parse_trades(msg):
	instr_match = re.search(r'TRADE ALERT\n([A-Za-z/]*)(?:\sAND\s)?([A-Za-z/]*)', msg)
	if instr_match:
		return instr_match.groups()
	return ()

maildir = mailbox.Maildir('/Users/andrew/.getmail/trade-alerts')

for msg in maildir:
	body = get_email_body(msg)
	match = regex.search(body)
	if match:
		print(match.groupdict())
	else:
		print('no match')


