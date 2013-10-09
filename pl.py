import quopri
import html.parser
import mailbox
import re
import pdb

def get_email_body(email_message):
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


regex = re.compile(r'.*(?P<direction>long|short) (?P<instrument>[A-Z/]*) @ (?P<entry>[0-9]*[.,]?[0-9]+).*protective stop @ (?P<stop>[0-9]*[.,]?[0-9]+)')


def parse_trade_alert(msg):
	def price_to_pips(price):
		# remove dots and commas to turn large numbers and decimals into pips
		stripped = re.sub(r'(\d+)[,.](\d+)', r'\1\2', price)
		return int(stripped)

	multi_move_stop_match = re.search(
		r'([A-Z/]*)(?:\sAND\s)?([A-Z/]*)\n.*moving protective stops.*to ([0-9]*[.,]?[0-9]+) and ([0-9]*[.,]?[0-9]+)',
		msg, re.IGNORECASE)

	commands = []

	if multi_move_stop_match:
		groups = multi_move_stop_match.groups()
		commands.append(MoveStop(groups[0], 'SHORT', price_to_pips(groups[2])))
		commands.append(MoveStop(groups[1], 'SHORT', price_to_pips(groups[3])))

	for match in regex.finditer(msg):
		price = price_to_pips(match.group('entry'))
		stop = price_to_pips(match.group('stop'))
		commands.append(OpenTrade(match.group('instrument'), match.group('direction'), price, stop))

	return commands


maildir = mailbox.Maildir('/Users/andrew/.getmail/trade-alerts')

for msg in maildir:
	body = get_email_body(msg)
	match = regex.search(body)
	print(body)
# if match:
# 	match.groupdict()
# else:
# 	print(body)


class OpenTrade:
	def __init__(self, instrument, direction, price, stop):
		self.instrument = instrument
		self.direction = direction
		self.price = price
		self.stop = stop

	def apply(self, trades):
		trades.append(Trade(self.instrument, self.direction, self.price, self.stop))


class CloseTrade:
	def __init__(self, instrument, price, account):
		self.instrument = instrument
		self.price = price
		self.account = account

	def apply(self, trades):
		trade = next((t for t in trades if t.instrument == self.instrument), None)
		trade.close(self.price)


class MoveStop:
	def __init__(self, instrument, direction, stop):
		self.instrument = instrument
		self.direction = direction
		self.stop = stop


class Trade:
	def __init__(self, instrument, direction, opening, stop):
		self.instrument = instrument
		self.direction = direction
		self.opening = opening
		self.stop = stop
		self.closing = None

	def close(self, price):
		self.closing = price

	def isopen(self):
		return self.closing == None

	def pl(self):
		return self.closing - self.opening


class BackTestResult:
	pass


class BackTest:
	def run(self, trade_alerts):
		trades = list()
		for alert in trade_alerts:
			alert.apply(trades)
		result = BackTestResult()
		result.pips = sum([t.pl() for t in trades])
		return result



