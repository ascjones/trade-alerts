import datetime
from pl import *

class TestTradeAlertGetCommands:
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

