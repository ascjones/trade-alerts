import pdb
import datetime
from colorama import init, Fore
import numpy as np

def get_last_trade(trades, instrument):
	return next((t for t in trades[::-1] if t.instrument == instrument and t.isopen()), None)

class OpenTrade:
	def __init__(self, instrument, direction, price, stop, date):
		self.instrument = instrument
		self.direction = direction
		self.price = price
		self.stop = stop
		self.date = date

	def apply(self, trades, all_accounts):
		existing_trade = get_last_trade(trades, self.instrument)
		if existing_trade and existing_trade.isopen():
			print(Fore.MAGENTA + 'Closing existing {} {} trade, assuming we have been stopped out'
				.format(existing_trade.direction, existing_trade.instrument) + Fore.RESET)
			existing_trade.close('STOP', all_accounts, self.date)
		trades.append(Trade(self.instrument, self.direction, self.price, self.stop, self.date, all_accounts))


class CloseTrade:
	def __init__(self, instrument, price, accounts, date, **kwargs):
		self.instrument = instrument
		self.price = price
		self.accounts = accounts
		self.date = date
		self.kwargs = kwargs

	def apply(self, trades, all_accounts):
		trade = get_last_trade(trades, self.instrument)
		if trade:
			accounts_to_close = all_accounts if self.accounts == 'ALL' else [acc for acc in all_accounts if acc.name in self.accounts]
			trade.close(self.price, accounts_to_close, self.date, self.kwargs)
		else:
			print(Fore.RED + 'Failed to close trade for {0} at {1} for accounts {2}: No previous trade found'.format(
				self.instrument, self.price, self.accounts) + Fore.RESET)

class MoveStop:
	def __init__(self, instrument, stop, date):
		self.instrument = instrument
		self.stop = stop
		self.date = date

	def apply(self, trades, accounts):
		trade = get_last_trade(trades, self.instrument)
		if trade:
			trade.move_stop(self.stop, self.date)
		else:
			print(Fore.RED + 'Failed to move stop for {0} to {1}: No previous trade found'.format(
				self.instrument, self.stop) + Fore.RESET)


class Account:
	def __init__(self, name):
		self.name = name
		self.pips = 0
		# todo: add ledger?

	def adjust(self, pl):
		self.pips += pl

	def __repr__(self):
		return 'Acc {}: {}'.format(self.name, self.pips)


def date_from_str(date_str):
		datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

class Trade:

	def __init__(self, instrument, direction, opening, stop, date, all_accounts):
		self.instrument = instrument
		self.direction = direction
		self.opening = opening
		self.stop = stop
		self.date = date if isinstance(date, datetime.datetime) else date_from_str(date)
		self.all_accounts = all_accounts
		self.accounts_pl = {}
		self.closing_prices = {}

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

	def close(self, price, accounts, date, kwargs=None):
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

		open_accounts = [a for a in self.all_accounts if a.name not in self.closing_prices.keys()]
		accounts_to_close = [a for a in open_accounts if a in accounts]
		account_pls = []
		total_pl = 0

		for account in accounts_to_close:
			self.closing_prices[account.name] = price
			pl = price - self.opening if self.direction == 'LONG' else self.opening - price
			self.accounts_pl[account.name] = pl
			account_pls.append((account.name, pl))
			total_pl += pl
			account.adjust(pl)

		pl_color = Fore.GREEN if total_pl > 0 else Fore.RED

		account_names = ','.join([acc.name for acc in accounts])
		account_pls = ' '.join(['{}: {:>4}'.format(acc_pl[0], acc_pl[1]) for acc_pl in account_pls])
		print('{}{:<13} {:<13} {:<6} @ {:<6} for accounts {:<16}{}P/L: {}{}'.format(
			Fore.YELLOW, 'Trade Closed:', self.instrument, self.direction, price, account_names, pl_color, account_pls, Fore.RESET))

	def move_stop(self, stop, date):
		prev_stop = self.stop
		if stop == 'BREAK EVEN':
			stop = self.opening
		self.stop = stop

		print('{}{:<13} {:<13} {:<6} from {} to {}{}'.format(
			Fore.MAGENTA, 'Stop Moved:', self.instrument, self.direction, prev_stop, self.stop, Fore.RESET))

	def isopen(self):
		return all([a.name in self.closing_prices.keys() for a in self.all_accounts]) == False

	def pl(self):
		return self.accounts_pl

	def total_pl(self):
		return sum([pl for acc, pl in self.accounts_pl.items()])
