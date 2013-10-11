import pdb
from colorama import init, Fore

class OpenTrade:
	def __init__(self, instrument, direction, price, stop):
		self.instrument = instrument
		self.direction = direction
		self.price = price
		self.stop = stop

	def apply(self, trades):
		trades.append(Trade(self.instrument, self.direction, self.price, self.stop))


class CloseTrade:
	def __init__(self, instrument, price, accounts, **kwargs):
		self.instrument = instrument
		self.price = price
		self.accounts = accounts
		self.kwargs = kwargs

	def apply(self, trades):
		trade = next((t for t in trades[::-1] if t.instrument == self.instrument), None)
		if trade:
			trade.close(self.price, self.accounts, self.kwargs)
		else:
			print(Fore.RED + 'Failed to close trade for {0} at {1} for accounts {2}: No previous trade found'.format(
				self.instrument, self.price, self.accounts) + Fore.RESET)

class MoveStop:
	def __init__(self, instrument, stop):
		self.instrument = instrument
		self.stop = stop

	def apply(self, trades):
		trade = next((t for t in trades[::-1] if t.instrument == self.instrument), None)
		if trade:
			trade.move_stop(self.stop)
		else:
			print(Fore.RED + 'Failed to move stop for {0} to {1}: No previous trade found'.format(
				self.instrument, self.stop) + Fore.RESET)

class Trade:
	def __init__(self, instrument, direction, opening, stop):
		self.instrument = instrument
		self.direction = direction
		self.opening = opening
		self.stop = stop
		self.closing = None

		if stop:
			self.risk = opening - stop if self.direction == 'LONG' else stop - opening
		else:
			self.risk = 'MAX'

		print('{:<13} {:<13} {:<6} @ {:<6} Stop: {:<6} Risk: {:<4}'.format(
			'Trade Opened:', self.instrument, self.direction, self.opening, self.stop, self.risk))

	def close(self, price, accounts, kwargs):
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

		self.closing = price
		pl = self.pl()
		pl_color = Fore.GREEN if pl > 0 else Fore.RED

		print('{}{:<13} {:<13} {:<6} @ {:<6} for accounts {:<6}{}P/L: {}{}'.format(
			Fore.YELLOW, 'Trade Closed:', self.instrument, self.direction, self.closing, accounts, pl_color, pl, Fore.RESET))

	def move_stop(self, stop):
		prev_stop = self.stop
		if stop == 'BREAK EVEN':
			stop = self.opening
		self.stop = stop

		print('{}{:<13} {:<13} {:<6} from {} to {}{}'.format(
			Fore.MAGENTA, 'Stop Moved:', self.instrument, self.direction, prev_stop, self.stop, Fore.RESET))

	def isopen(self):
		return self.closing == None

	def pl(self):
		return self.closing - self.opening if self.direction == 'LONG' else self.opening - self.closing