import pl

def test_double_trade():
	body = 'TRADE ALERT\nDOW AND FTSE\nI am moving protective stops on shorts to 15,298 and 6648 resp.\nUSD/JY\nI have just gone long USD/JY @ 97.20 with protective stop @ 96.20 for\na 100 pip risk.\nJohn\n\n\n'
	trades = pl.parse_trades(body)
	assert len(trades) == 2