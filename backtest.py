from model import *
import alerts

def run_backtest(trade_alerts):
	trades = []
	for alert in trade_alerts:
		alert.apply(trades)

if __name__ == '__main__':
	run_backtest(alerts.trade_alerts)