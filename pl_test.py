from pl import *

class TestParseTradeAlerts:
	def test_double_trade(self):
		body = 'TRADE ALERT\nDOW AND FTSE\nI am moving protective stops on shorts to 15,298 and 6648 resp.\nUSD/JY\nI have just gone long USD/JY @ 97.20 with protective stop @ 96.20 for\na 100 pip risk.\nJohn\n\n\n'
		commands = parse_trade_alert(body)
		assert len(commands) == 3
		assert isinstance(commands[0], MoveStop)
		assert isinstance(commands[1], MoveStop)

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

