from model import *
import backtest
import datetime

default_date = datetime.datetime.now()

def assert_trade(trade, **kwargs):
	trade_vars = vars(trade)
	for key, value in kwargs.items():
		assert trade_vars[key] == value

def all_accounts_pl(pl):
	return {'A':pl, 'B':pl, 'C':pl}

def test_relative_pl():
	alerts = [
		OpenTrade('USD/JY', 'LONG', 9900, 9880, default_date),
		CloseTrade('USD/JY', None, ['B'], default_date, pl=300)
	]
	trades = backtest.run_backtest(alerts).trades
	assert len(trades) == 1
	assert_trade(trades[0], instrument='USD/JY', direction='LONG', opening=9900, stop=9880, risk=9900 - 9880, closing_prices={'B': 9900 + 300})
	assert trades[0].pl() == {'B': 300}

def test_pl_multiple_trades():
	alerts = [
		OpenTrade('USD/JY', 'LONG', 9900, 9880, default_date),
		CloseTrade('USD/JY', 10000, 'ALL', default_date),
		OpenTrade('USD/JY', 'LONG', 10000, 9900, default_date),
		CloseTrade('USD/JY', 9900, 'ALL', default_date)
	]
	trades = backtest.run_backtest(alerts).trades
	assert len(trades) == 2
	assert_trade(trades[0], instrument='USD/JY', direction='LONG', opening=9900, stop=9880, closing_prices=all_accounts_pl(10000))
	assert_trade(trades[1], instrument='USD/JY', direction='LONG', opening=10000, stop=9900, closing_prices=all_accounts_pl(9900))

def test_short_trade_pl():
	alerts = [
		OpenTrade('DOW', 'SHORT', 15000, 15100, default_date),
		CloseTrade('DOW', 14900, 'ALL', default_date)
	]
	trades = backtest.run_backtest(alerts).trades
	assert len(trades) == 1
	assert trades[0].pl() == all_accounts_pl(100)

def test_close_separate_accounts():
	alerts = [
		OpenTrade('DOW', 'SHORT', 15000, 15100, default_date),
		CloseTrade('DOW', 14900, ['A'], default_date),
		CloseTrade('DOW', 14800, ['B'], default_date),
	]
	trades = backtest.run_backtest(alerts).trades
	assert len(trades) == 1
	assert trades[0].pl()['A'] == 100
	assert trades[0].pl()['B'] == 200

def test_close_existing_trade_when_new_trade_for_same_instrument():
	alerts = [
		OpenTrade('DOW', 'SHORT', 15000, 15100, default_date),
		OpenTrade('DOW', 'SHORT', 15100, 15200, default_date),
	]
	result = backtest.run_backtest(alerts).trades
	assert len(trades) == 2
	assert_trade(trades[0], closing_prices=all_accounts_pl(15100))
	assert_trade(trades[1], opening=15100, stop=15200)

def test_calculate_pl_from_all_trades():
	alerts = [
		OpenTrade('DOW', 'SHORT', 15000, 15100, default_date),
		OpenTrade('DOW', 'SHORT', 15100, 15200, default_date),
		OpenTrade('GOLD', 'LONG', 13400, 13300, default_date),
		CloseTrade('GOLD', 13500, 'ALL', default_date),
		CloseTrade('DOWN', 14900, 'ALL', default_date)
	]
	result = backtest.run_backtest(alerts)
	assert = result.account_pl('A') == 200
	assert = result.total_pl() == 600
