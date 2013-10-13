from model import *
import alerts
from collections import defaultdict
import sys

class BackTestResult:
	def __init__(self, trades, accounts):
		self.trades = trades
		self.accounts = accounts

	def account_pl(self, acc_name):
		acc = [a for a in self.accounts if a.name == acc_name][0]
		return acc.pips

	def instruments_pl(self):
		pl_by_instr = defaultdict(lambda: defaultdict(lambda: 0))
		for t in self.trades:
			for acc, pl in t.pl().items():
				pl_by_instr[t.instrument][acc] += pl
		return pl_by_instr

	def total_pl(self):
		return sum([a.pips for a in self.accounts])

	def __str__(self):

		total = len(self.trades)
		longs = len([t for t in self.trades if t.direction == 'LONG'])
		shorts = total - longs

		def perc(trade_count):
			return (trade_count / total) * 100

		result = ''' 
Trades: {}
Long:   {} ({}%)
Short:  {} ({}%)
P/L: A:{}, B:{}, C:{}, Total: {}\n\n'''.format(
	total, longs, perc(longs), shorts, perc(shorts), self.account_pl('A'), self.account_pl('B'), self.account_pl('C'), self.total_pl())

		result += '\n'.join(
			['{:<13} {}'.format(instr, '\t'.join(
				'{}:{:>5}'.format(acc, pl) for acc, pl in sorted(pls.items()) )) for instr, pls in self.instruments_pl().items()])
		return result


class BackTest:
	def __init__(self):
		self.accounts = [Account('A'), Account('B'), Account('C')]

	def run(self, trade_alerts, instruments=None):
		trades = []
		for alert in trade_alerts:
			if instruments == None or alert.instrument in instruments:
				alert.apply(trades, self.accounts)


		return BackTestResult(trades, self.accounts)

if __name__ == '__main__':
	backtest = BackTest()
	instr = sys.argv[1] if len(sys.argv) == 2 else None

	print('================================================================================\n')
	result = backtest.run(alerts.trade_alerts, instr)
	print(result)
	print('================================================================================\n')