import pdb

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
		trade = next((t for t in trades if t.instrument == self.instrument), None)
		if trade:
			trade.close(self.price, self.accounts, self.kwargs)
		else:
			print('Failed to close trade for {0} at {1} for accounts {2}: No previous trade found'.format(
				self.instrument, self.price, self.accounts))

class MoveStop:
	def __init__(self, instrument, stop):
		self.instrument = instrument
		self.stop = stop

	def apply(self, trades):
		trade = next((t for t in trades if t.instrument == self.instrument), None)
		if trade:
			trade.move_stop(self.stop)
		else:
			print('Failed to move stop for {0} to {1}: No previous trade found'.format(
				self.instrument, self.stop))

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
		print('Trade Opened: {0} {1} @ {2}, Stop {3} for {4} pip risk'.format(self.instrument, self.direction, self.opening, self.stop, self.risk))

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
		print('Trade Closed: {0} {1} @ {2} for accounts {3}. P/L {4}'.format(self.instrument, self.direction, self.closing, accounts, self.pl()))

	def move_stop(self, stop):
		prev_stop = self.stop
		if stop == 'BREAK EVEN':
			stop = self.opening
		self.stop = stop
		print('Stop Moved: {0} {1} from {2} to {3}'.format(self.instrument, self.direction, prev_stop, self.stop))

	def isopen(self):
		return self.closing == None

	def pl(self):
		return self.closing - self.opening