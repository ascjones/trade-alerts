import re
import quopri
import html.parser
import email.utils
import mailbox
import datetime
import pdb
from model import *

class TradeAlert:
	def __init__(self, msg, date):
		self.msg = msg
		self.date = date

	regex = re.compile(
		r'.*(?P<direction>long|short\w*) (?P<instrument>[A-Z/]*) @ (?P<entry>[0-9]*[.,]?[0-9]+).*protective stop @ (?P<stop>[0-9]*[.,]?[0-9]+)', 
		re.IGNORECASE)

	def get_commands(self):
		def price_to_pips(price):
			# remove dots and commas to turn numbers and decimals into pips
			stripped = re.sub(r'(\d+)[,.](\d+)', r'\1\2', price)
			return int(stripped)

		commands = []

		move_stop_match = re.search(
			r'([A-Z/]*)\n.*moving my stop to ([0-9]*[.,]?[0-9]+) for ([ABC]) and ([ABC]) accounts', self.msg, re.IGNORECASE)

		if move_stop_match:
			instrument = move_stop_match.group(1)
			stop = price_to_pips(move_stop_match.group(2))
			accounts = [move_stop_match.group(3), move_stop_match.group(4)]
			commands.append(MoveStop(instrument, stop, accounts))

		multi_move_stop_match = re.search(
			r'([A-Z/]*)(?:\sAND\s)?([A-Z/]*)\n.*moving protective stops.*to ([0-9]*[.,]?[0-9]+) and ([0-9]*[.,]?[0-9]+)',
			self.msg, re.IGNORECASE)

		if multi_move_stop_match:
			groups = multi_move_stop_match.groups()
			commands.append(MoveStop(groups[0], price_to_pips(groups[2]), 'ALL'))
			commands.append(MoveStop(groups[1], price_to_pips(groups[3]), 'ALL'))

		for match in self.regex.finditer(self.msg):
			price = price_to_pips(match.group('entry'))
			stop = price_to_pips(match.group('stop'))
			instrument = match.group('instrument').upper()
			direction = 'LONG' if re.match(r'long', match.group('instrument')) else 'SHORT'
			commands.append(OpenTrade(instrument, direction, price, stop))
		return commands

	def is_trade_alert(self):
		return re.match(r'TRADE ALERT.*', self.msg, re.MULTILINE) != None


def create_trade_alert(email_message):
	
	def get_body():
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

	def get_date():
		date_str = email_message.get('date')
		date_tuple = email.utils.parsedate_tz(date_str)
		return datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))

	return TradeAlert(get_body().strip('\n'), get_date())

if __name__ == "__main__":

	maildir = mailbox.Maildir('/Users/andrew/.getmail/trade-alerts')
	trade_alerts = sorted([create_trade_alert(msg) for msg in maildir], key=lambda m: m.date)

	# with open('/Users/andrew/code/trade-alerts/trades.txt', 'w') as f:
	# 	for ta in trade_alerts:
	# 		f.write('----------------------------------------------------\n')
	# 		f.write(ta.msg + '\n')
	# 		f.write('----------------------------------------------------\n')

	actual_trade_alerts = [ta for ta in trade_alerts if ta.is_trade_alert()]
	not_trade_alerts = [ta for ta in trade_alerts if ta.is_trade_alert() == False]
	print('All: {0}, True: {1}, False: {2}'.format(len(trade_alerts), len(actual_trade_alerts), len(not_trade_alerts)))

	# print all OpenTrades to file
	with open('/Users/andrew/code/trade-alerts/trades.txt', 'w') as f:
		for ta in trade_alerts:
			commands = ta.get_commands()
			f.write('----------------------------------------------------\n')
			f.write(ta.msg + '\n')
			for c in commands:
					if isinstance(c, OpenTrade):
						f.write("OpenTrade('{0}', '{1}', {2}, {3})\n".format(c.instrument, c.direction, c.price, c.stop))
			f.write('----------------------------------------------------\n')
