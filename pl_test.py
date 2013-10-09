from pl import *

def test_double_trade():
	body = 'TRADE ALERT\nDOW AND FTSE\nI am moving protective stops on shorts to 15,298 and 6648 resp.\nUSD/JY\nI have just gone long USD/JY @ 97.20 with protective stop @ 96.20 for\na 100 pip risk.\nJohn\n\n\n'
	trades = parse_trades(body)
	assert len(trades) == 2

def test_long_trade_profit():
	opentrade = OpenTradeAlert('GBP/USD', 'LONG', 15210, 15160)
	closetrade = CloseTradeAlert('GBP/USD', 15310, 'A')
	backtest = BackTest()
	pl = backtest.run([opentrade, closetrade])
	assert pl.pips == 100

def test_long_trade_loss():
	opentrade = OpenTradeAlert('GBP/USD', 'LONG', 15210, 15160)
	closetrade = CloseTradeAlert('GBP/USD', 15200, 'A')
	backtest = BackTest()
	pl = backtest.run([opentrade, closetrade])
	assert pl.pips == -10	

