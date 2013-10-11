import mailbox
import fileinput
import email.utils
import datetime
import re

def insert_dates():
	def get_date(msg):
		date_str = msg.get('date')
		date_tuple = email.utils.parsedate_tz(date_str)
		return datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))

	maildir = mailbox.Maildir('/Users/andrew/.getmail/trade-alerts')
	dates = sorted([get_date(msg) for msg in maildir])

	curr_date_i = 0
	for line in fileinput.input('/Users/andrew/code/trade-alerts/alerts.py', inplace=1):
		if re.match('^# John', line):
			# end of current Trade Alert move to next date
			curr_date_i += 1
		date = dates[curr_date_i]
		line = re.sub(r'^(?!#)(.*)(\))', r'\1, "{}")'.format(date.isoformat()), line.rstrip())
		print(line)

if __name__ == '__main__':
	insert_dates()
