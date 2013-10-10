import datetime
from pl import *

class TestTradeAlertGetCommands:
	def test_short_trade(self):
		alert = TradeAlert(
			'TRADE ALERT\nDOW\nI am going out on a limb a little here, but..\n'
			'I have shorted Dow @ 14,950 with protective stop @ 15,010 for a 60 pip\nrisk.\nJohn\n\n\n', None)
		commands = alert.get_commands()
		assert len(commands) == 1
		assert isinstance(commands[0], OpenTrade)
		assert commands[0].instrument == 'DOW'
		assert commands[0].direction == 'SHORT'
		assert commands[0].price == 14950
		assert commands[0].stop == 15010

	def test_move_stops(self):
		alert = TradeAlert(
			'TRADE ALERT\nUSD/JY\n'
			'I am moving my stop to 99.00 for B and C Accounts to lock in nice\ngains with potential for more!\nJohn', None)
		commands = alert.get_commands()
		assert len(commands) == 1
		assert isinstance(commands[0], MoveStop)
		assert commands[0].instrument == 'USD/JY'
		assert commands[0].stop == 9900
		assert commands[0].accounts == ['B', 'C']

	def test_double_trade(self):
		alert = TradeAlert(
			'TRADE ALERT\nDOW AND FTSE\nI am moving protective stops on shorts to 15,298 and 6648 resp.\n'
			'USD/JY\nI have just gone long USD/JY @ 97.20 with protective stop @ 96.20 for\na 100 pip risk.\nJohn\n\n\n', None)
		commands = alert.get_commands()
		assert len(commands) == 3
		assert isinstance(commands[0], MoveStop)
		assert isinstance(commands[1], MoveStop)
		assert isinstance(commands[2], OpenTrade)

class TestBackTest:
	def test_long_trade_profit(self):
		opentrade = OpenTrade('GBP/USD', 'LONG', 15210, 15160)
		closetrade = CloseTrade('GBP/USD', 15310, 'A')
		backtest = BackTest()
		pl = backtest.run([opentrade, closetrade])
		assert pl.pips == 100

	def test_long_trade_loss(self):
		opentrade = OpenTrade('GBP/USD', 'LONG', 15210, 15160)
		closetrade = CloseTrade('GBP/USD', 15200, 'A')
		backtest = BackTest()
		pl = backtest.run([opentrade, closetrade])
		assert pl.pips == -10	

