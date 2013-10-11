from model import *
import alerts

class BackTestResult:
	def __init__(self, trades, pl):
		self.trades = trades
		self.pl = pl

def run_backtest(trade_alerts):
	trades = []
	for alert in trade_alerts:
		alert.apply(trades)
	return BackTestResult(trades, None)

if __name__ == '__main__':
	run_backtest(alerts.trade_alerts)
	print('================================================================================\n')