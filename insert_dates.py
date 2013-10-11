import fileinput

def insert_dates():

	maildir = mailbox.Maildir('/Users/andrew/.getmail/trade-alerts')
	trade_alerts = sorted([create_trade_alert(msg) for msg in maildir], key=lambda m: m.date)
	dates = [ta.date for ta in trade_alerts]

	cmd_re = re.compile(r'')

	urr_date_i = 0
	for line in fileinput.input('/Users/andrew/code/trade-alerts/alerts.py', inplace=1):
		if re.match('^# John', string):
			# end of current Trade Alert move to next date
			curr_date_i++
		date = dates[curr_date_i]
		line = re.sub(r'^[^#].*(\),)', '"{}"),'.format(date.isoformat()), line.rstrip())
		print(line)

if __name__ == '__main__':
	insert_dates()
