from model import *
import alerts

class BackTestResult:
	def __init__(self, trades, pl):
		self.trades = trades
		self.pl = pl


def run_backtest(trade_alerts):
	trades = []
	accounts = [Account('A'), Account('B'), Account('C')]
	for alert in trade_alerts:
		alert.apply(trades, accounts)

	# accounts_pl = dict({'A': 0, 'B': 0, 'C': 0})
	# for trade in trades:
	# 	for acc, pl in accounts_pl:
	# 		if acc in trade.closing_prices.keys()
	# 			accou

	return BackTestResult(trades, None)

if __name__ == '__main__':
	run_backtest(alerts.trade_alerts)
	print('================================================================================\n')