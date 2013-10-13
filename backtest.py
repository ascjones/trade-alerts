from model import *
import alerts

class BackTestResult:
	def __init__(self, trades, accounts):
		self.trades = trades
		self.accounts = accounts

	def account_pl(self, acc_name):
		acc = [a for a in self.accounts if a.name == acc_name][0]
		return acc.pips

	def total_pl(self):
		return sum([a.pips for a in self.accounts])

	def __str__(self):

		total = len(self.trades)
		longs = len([t for t in self.trades if t.direction == 'LONG'])
		shorts = total - longs

		def perc(trade_count):
			return (trade_count / total) * 100

		return r''' 
Trades: {}
Long:   {} ({}%)
Short:  {} ({}%)
P/L: A:{}, B:{}, C:{}, Total: {}'''.format(
	total, longs, perc(longs), shorts, perc(shorts), self.account_pl('A'), self.account_pl('B'), self.account_pl('C'), self.total_pl())

class BackTest:
	def __init__(self):
		self.accounts = [Account('A'), Account('B'), Account('C')]

	def run(self, trade_alerts, instruments=None):
		trades = []
		for alert in trade_alerts:
			if instruments == None or alert.instrument in instruments:
				alert.apply(trades, self.accounts)

		# accounts_pl = dict({'A': 0, 'B': 0, 'C': 0})
		# for trade in trades:
		# 	for acc, pl in accounts_pl:
		# 		if acc in trade.closing_prices.keys()
		# 			accou

		return BackTestResult(trades, self.accounts)

if __name__ == '__main__':
	backtest = BackTest()
	result = backtest.run(alerts.trade_alerts) #, ['USD/JY'])
	print(result)

	print('================================================================================\n')