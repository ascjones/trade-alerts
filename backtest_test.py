from model import *
import backtest

def test_relative_pl():
	alerts = [
		OpenTrade('USD/JY', 'LONG', 9900, 9880),
		CloseTrade('USD/JY', None, ['B'], pl=300)
	]
	backtest.run_backtest(alerts)