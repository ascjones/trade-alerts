import quopri
import html.parser
import mailbox
import email.utils

def get_body(email_message):
	def to_utf(part):
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
				return to_utf(part)
			elif maintype == 'text':
				return to_utf(email_message)
	else:
		return to_utf(email_message)


def get_date(self):
	date_tuple=email.utils.parsedate_tz(date_str)
    return datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))