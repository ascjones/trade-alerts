from model import *
import backtest

def assert_trade(trade, **kwargs):
	trade_vars = vars(trade)
	for key, value in kwargs.items():
		assert trade_vars[key] == value

def test_relative_pl():
	alerts = [
		OpenTrade('USD/JY', 'LONG', 9900, 9880),
		CloseTrade('USD/JY', None, ['B'], pl=300)
	]
	trades = backtest.run_backtest(alerts)
	assert len(trades) == 1
	assert_trade(trades[0], instrument='USD/JY', direction='LONG', opening=9900, stop=9880, risk=9900 - 9880, closing=9900 + 300)
	assert trades[0].pl() == 300

def test_pl_multiple_trades():
	alerts = [
		OpenTrade('USD/JY', 'LONG', 9900, 9880),
		CloseTrade('USD/JY', 10000, 'ALL'),
		OpenTrade('USD/JY', 'LONG', 10000, 9900),
		CloseTrade('USD/JY', 9900, 'ALL')
	]
	trades = backtest.run_backtest(alerts)
	assert len(trades) == 2
	assert_trade(trades[0], instrument='USD/JY', direction='LONG', opening=9900, stop=9880, closing=10000)
	assert_trade(trades[1], instrument='USD/JY', direction='LONG', opening=10000, stop=9900, closing=9900)

def test_short_trade_pl():
	alerts = [
		OpenTrade('DOW', 'SHORT', 15000, 15100),
		CloseTrade('DOW', 14900, 'ALL')
	]
	trades = backtest.run_backtest(alerts)
	assert len(trades) == 1
	assert trades[0].pl() == 100
