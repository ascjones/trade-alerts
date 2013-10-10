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
	def __init__(self, instrument, stop):
		self.instrument = instrument
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