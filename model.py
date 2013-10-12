import pdb
import datetime
from colorama import init, Fore

class OpenTrade:
	def __init__(self, instrument, direction, price, stop, date):
		self.instrument = instrument
		self.direction = direction
		self.price = price
		self.stop = stop
		self.date = date

	def apply(self, trades):
		trades.append(Trade(self.instrument, self.direction, self.price, self.stop, self.date))


class CloseTrade:
	def __init__(self, instrument, price, accounts, date, **kwargs):
		self.instrument = instrument
		self.price = price
		self.accounts = accounts
		self.date = date
		self.kwargs = kwargs

	def apply(self, trades):
		trade = next((t for t in trades[::-1] if t.instrument == self.instrument), None)
		if trade:
			trade.close(self.price, self.accounts, self.date, self.kwargs)
		else:
			print(Fore.RED + 'Failed to close trade for {0} at {1} for accounts {2}: No previous trade found'.format(
				self.instrument, self.price, self.accounts) + Fore.RESET)

class MoveStop:
	def __init__(self, instrument, stop, date):
		self.instrument = instrument
		self.stop = stop
		self.date = date

	def apply(self, trades):
		trade = next((t for t in trades[::-1] if t.instrument == self.instrument), None)
		if trade:
			trade.move_stop(self.stop, self.date)
		else:
			print(Fore.RED + 'Failed to move stop for {0} to {1}: No previous trade found'.format(
				self.instrument, self.stop) + Fore.RESET)

def date_from_str(date_str):
		datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

class Trade:

	def __init__(self, instrument, direction, opening, stop, date):
		self.instrument = instrument
		self.direction = direction
		self.opening = opening
		self.stop = stop
		self.closing_prices = {}
		self.date = date if isinstance(date, datetime.datetime) else date_from_str(date)

		if stop:
			if direction == 'LONG':
				if opening < stop:
					raise Exception('Invalid Stop for LONG trade. Entry {0} < Stop {1}'.format(opening, stop))
				self.risk = opening - stop
			elif direction == 'SHORT':
				if opening > stop:
					raise Exception('Invalid Stop for SHORT trade. Entry {0} > Stop {1}'.format(opening, stop))
				self.risk = stop - opening
		else:
			self.risk = 'MAX'

		print('{:<13} {:<13} {:<6} @ {:<6} Stop: {:<6} Risk: {:<4}'.format(
			'Trade Opened:', self.instrument, self.direction, self.opening, self.stop, self.risk))

	account_ids = ['A','B','C']

	def close(self, price, accounts, date, kwargs):
		if price == 'STOP':
			price = self.stop
		elif price == 'BREAK EVEN':
			price = self.opening
		elif price == None:
			if kwargs['pl']:
				price = self.opening + kwargs['pl']
			else:
				raise Exception('No closing price or P/L specified for {0} {1}'.format(self.instrument))
		elif isinstance(price, str):
			raise Exception('Unsupported closing price {0}'.format(price))

		# if 'ALL' accounts then close remaining open accounts
		open_accounts = [a for a in self.account_ids if a not in self.closing_prices.keys()]
		accounts_to_close = open_accounts if accounts == 'ALL' else accounts

		for account in accounts_to_close:
			self.closing_prices[account] = price

		accounts_pl = dict([accpl for accpl in self.pl().items() if accpl[0] in accounts_to_close])
		total_pl = sum(accounts_pl.values())
		pl_color = Fore.GREEN if total_pl > 0 else Fore.RED

		print('{}{:<13} {:<13} {:<6} @ {:<6} for accounts {:<16}{}P/L: {}{}'.format(
			Fore.YELLOW, 'Trade Closed:', self.instrument, self.direction, price, accounts, pl_color, accounts_pl, Fore.RESET))

	def move_stop(self, stop, date):
		prev_stop = self.stop
		if stop == 'BREAK EVEN':
			stop = self.opening
		self.stop = stop

		print('{}{:<13} {:<13} {:<6} from {} to {}{}'.format(
			Fore.MAGENTA, 'Stop Moved:', self.instrument, self.direction, prev_stop, self.stop, Fore.RESET))

	def isopen(self):
		return self.closing == None

	def pl(self):
		accounts_pl = {}
		for account, closing in self.closing_prices.items():
			accounts_pl[account] = closing - self.opening if self.direction == 'LONG' else self.opening - closing
		return accounts_pl