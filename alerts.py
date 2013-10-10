from model import *

trade_alerts = [
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I am going out on a limb a little here, but..
# I have shorted Dow @ 14,950 with protective stop @ 15,010 for a 60 pip
# risk.
OpenTrade('DOW', 'SHORT', 14950, 15010),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I am moving my stop to 99.00 for B and C Accounts to lock in nice
MoveStop('USD/JY', 9900),
# gains with potential for more!
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have shorted EUR/USD @ 1.3110 with protective stop @ 1.3160 for a 50
OpenTrade('EUR/USD', 'SHORT', 13110, 13160),
# pip risk.
# I will have a new post on FMT shortly.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# AUS/USD
# I have taken profit for A Account on AUS/USD @ 10160 for a 100 pip
# profit.
CloseTrade('AUS/USD', 10160, ['A']),
# Also, stops on USD/JY were elected today and profits taken for B and C
CloseTrade('USD/JY', 'STOP', ['B', 'C']),
# Accounts of 165 pips..
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT

# 1. I have shorted USD/JY @ 99.00 with protective stop @ 99.40 for a 40
# pip risk.  FAST MARKET.
OpenTrade('USD/JY', 'SHORT', 9900, 9940),
# 2.  I have shorted GBP/USD @ 155.10 with protective stop @  155.60
OpenTrade('GBP/USD', 'SHORT', 15510, 15560),
# for a 50 pip risk.  FAST MARKET
# Missed entry in gold - will attempt later.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# 1.  GOLD   I have bought (long) @ $1460 with stop @ $1450 for a 100
# pip risk
OpenTrade('GOLD', 'LONG', 14600, 14500),
# 2.  DOW  I have entered a stop order shorting @ 15,000.  If filled,
# I will enter buy stop @ 15,060.
# Charts in an upcoming FMT post this afternoon.
# John 
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# I have covered my shorts in
# EUR/USD @ 1.3130
CloseTrade('EUR/USD', 13130, 'ALL'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# JUNE T-BONDS
# I have a new long trade @ 146.30 with protective stop @ 145.80 for a
OpenTrade('JUNE T-BONDS', 'LONG', 14630, 14580),
# 50 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# 1.  I have cancelled order to short Dow @ 15,000 from yesterday (not
# filled)
# 2.  DOW  I have just shorted Dow @ 15,100 with protective stop @
# 15,160 for a 60 pip risk. My tramline is on the verge of being broken.
OpenTrade('DOW', 'SHORT', 15100, 15160),
# 3.  ALCOA   has had a mighty good run and I am exiting at the open
# today for A Account only.  This is a small contract, and so I have
CloseTrade('ALCOA', 'OPEN', 'A'),
# bet five times my usual.  When you see the updated Trading Record,
# you will see my bet @ 5  times the point move in pips. My entry was
# at 8.38 on 29 April. 
# I will post a new FMT later this morning with charts.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# The move down looks very corrective, which places the odds towards a
# new challenge of the 100 level.
# I am going to reverse out of my short trade and then go long if the
CloseTrade('USD/JY', 9894, 'ALL'),
# market hits 99.00 (currently 98.84).
# John
# ----------------------------------------------------
# ----------------------------------------------------
# NIKKEII have been following the Nikkei closely for some time and
# projected a move to the 14,000 area (a Fib level) - see my previous
# coverage.  The market has reached 14,000 and is currently trading
# slightly above it.
# The bullish tide has lifted all boats, including the Nikkei, which has
# doubled in just a few months.  This is an incredible performance,
# considering that Japanese stocks have been shunned for years until
# last year.  It shows what a change in sentiment can produce.
# And I believe there is a change in sentiment going on right now in
# equities from positive to negative.
# The Nikkei has formed patterns very similar to the Dow and S&P and
# this morning, it has broken through the lower tramline after a big neg
# mom div.  
# Will post a chart in my next FMT blog.
# I hope this is a significant omen for the Dow.  Jobless Claims out
# later today.
# I may have a Nikkei trade shortly.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# 1.  GOLD.. I have moved my stop to break even
MoveStop('GOLD', 'BREAK EVEN'),
# 2.  NIKKEI   I have just shorted Rolling Nikkei @ 14,190 with
# protective stop @ 14,290 for a 100 pip risk.
OpenTrade('NIKKEI', 'SHORT', 14190, 14290),
# Nice updated Nikkei chart in next FMT post.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADES
# 1.  I am now long USD/JY having reversed out of short @ 99.00
OpenTrade('USD/JY', 'LONG', 9900, None),
# 2.  Stopped out of long gold @ break even
CloseTrade('GOLD', 'STOP', 'ALL'),
# 3.  I am moving my stop on short Dow to 15,120
MoveStop('DOW', 15120),
# 4.  I am moving my stop on long T-Bonds to break-even.
MoveStop('JUNE T-BONDS', 'BREAK EVEN'),
# 5.  Stopped out of short Nikkei @ 14,295
CloseTrade('NIKKEI', 'STOP', 'ALL'),
# 6.  Exited Alcoa @  8.82  for A Account for big gain
CloseTrade('ALCOA', 882, ['A']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# Now trading at 99.35.
# I am entering protective stop @ 98.80
MoveStop('USD/JY', 9880),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT

# EUR/USD
# I have just shorted EUR/USD @ 1.3060 with protective stop @ 1.3140 for
OpenTrade('EUR/USD', 'SHORT', 13060, 13140),
# an 80 pip risk.
# Nice move on the USD/JY
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just shorted Dow @ 15,110 with protective stop : 15,160.
OpenTrade('DOW', 'SHORT', 15110, 15160),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have taken profit for A Account @ 1.0105
CloseTrade('USD/JY', 10105, ['A']),
# JUNE T-BONDS
# I have been stopped at break even.
CloseTrade('JUNE T-BONDS', 'BREAK EVEN', 'ALL'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# OK, I give in.
# DOW
# I have reversed from short to long at 15,110 with protective stop @
# 15,060
CloseTrade('DOW', 15110, 'ALL'),
OpenTrade('DOW', 'LONG', 15110, 15060),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# JUNE T-BONDS
# I HAVE JUST GONE LONG JUNE T-BONDS @ 145.70 WITH PROTECTIVE STOP @
# 145.20 FOR A 50 PIP RISK
OpenTrade('JUNE T-BONDS', 'LONG', 14570, 14520),
# EUR/USD
# I HAVE TAKEN PROFIT IN A ACCOUNT ON MY SHORT EUR/USD @ 1.3002
CloseTrade('EUR/USD', 13002, ['A']),
# AUS/USD
# I HAVE TAKEN PROFIT IN A ACCOUNT IN SHORT AUS/USD @ 1.0025
CloseTrade('AUS/USD', 10025, ['A']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# Yes, that was predictable!  When the last bear joins the party, the
# top is in.  It appears that way as I write.
# TRADE  I have just shorted Dow @ 15,065 with protective stop @ 15,165
# for a 100 pip risk.
OpenTrade('DOW', 'SHORT', 15065, 15165),
# TRADE  I have exited all Alcoa positions @ 8.64
CloseTrade('ALCOA', 864, 'ALL'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# Here is an excellent article [1]where the author is as baffled as I am
# re the disconnect between the US economy and the stock market.
# Enjoy!
# John



# Links:
# ------
# [1]
# http://seekingalpha.com/article/1423631-the-good-news-the-bad-news-and-what-s-very-ugly?source=email_macro_view&amp;ifp=0
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# If it can move above my trendline, a move to the $1480 area looks
# likely.
# TRADE    ENTER ORDER TO BUY GOLD @ $1438 ON STOP.  IF FILLED, ENTER
# PROTECTIVE STOP @ $1428 FOR A 100 PIP RISK.
# IF NOT DONE BY TONIGH'S CLOSE, THEN CXL.
# I will have a FMT post later today.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# Unable on yesterday's order, but I have just traded long @ $1438 with
# protective stop @ $1428
OpenTrade('GOLD', 'LONG', 14380, 14280),
# EUR/USD, AUS/USD
# I have just moved protective stops to break-even
MoveStop('EUR/USD', 'BREAK EVEN'),
MoveStop('AUS/USD', 'BREAK EVEN'),
# JUNE T-BONDS
# I have just placed order to buy @ 145.00 on stop.  If filled, will
# place protective stop @ 144.20 for an 80 pip risk.
# DOW
# is looking absolutely exhausted here and will start a big decline.  I
# am looking to add to short positions on a break of the 10,050 level,
# so stand by.
# Will have new FMT and MC posts later
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD.JY
# I have exited for B Account for 300 pip gain.
CloseTrade('USD/JY', None, ['B'], pl=300),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have exited my last remaining C Account position @ 1.0250
CloseTrade('USD/JY', 10250, ['C']),
# DOW
# I have entered a sell stop shorting Dow @  15,170.  If filled, my
# protective stop is at 15, 220 for a 50 pip risk
# GOLD
# I have just gone long gold @ $1410 with protective stop @ $1404 for a
# 60 pip risk.
OpenTrade('GOLD', 'LONG', 14100, 14040),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# APPLE
# I have just gone long Apple @ 434.50 with protective stop @ 428 for a
OpenTrade('APPLE', 'SHORT', 43450, 42800),
# 65 pip stop.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTSYesterday, I discovered that not all of my Trade Alerts
# are arriving at your inbox in a timely way.  If you have experienced
# any delay, please let me know. 
# If you receive a delayed email, you will likely notice my trade prices
# are different from that on your screen, but my entries and exits are
# genuine!  It does take me a few moments to compose the Alert, and in
# a fast market - which I try to avoid - prices may be somewhat
# different when you check.
# DOWYes, we are coming to the final top.  Latest sentiment readings
# are in the stratosphere.  Everyone is now on board  the rocket to
# the moon.  Yesterday, I had a W5 = W1 target in the S&P of 1644.
#  This morning, it is trading at 1655, slightly above.
# The equivalent target in the Dow is 14,364 - now at 15,250, so there
# is another 100 pips or so to go - if it makes it.
# This means the top could come at any time.  Stand by for fireworks.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have set an order shorting Dow @ 15,220 on stop.  If filled, I will
# set protective stop @ 15,320 forr a 100 pip risk.
# I will be away tomorrow at the MoneyWeek Conference and will have no
# Alerts, unless it is very early.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# WEEKLY WRAP
# I have posted my WR on my fts.com site today.  Click here to read.
# [1]
# Have a good weekend!
# John



# Links:
# ------
# [1] http://financialtradingstrategies.com/wpblog
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# 1.  EUR/USD  I have covered shorts in all accounts @ 1.2860 on a
CloseTrade('EUR/USD', 12860, 'ALL'),
# tramline break
# 2.  USD/JY   I have set an order to short USD/JY @ 101.80 on stop.
#  If filled, my stop will be at 102.60 for a 60 pip risk.
# Blogs and Trading Record will be updated later this morning.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/GBP
# I have just shorted EUR/GBP @ 0.8465 with protective stop @ 0.8490 for
OpenTrade('EUR/GBP', 'SHORT', 8465, 8490),
# a 25 pip risk
# Will have an update for FMT blog a little later.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# JUNE T-BONDS
# I have just shorted June T-Bonds @ 143.40 with protective stop @
# 144.20 for an 80 pip risk.
OpenTrade('JUNE T-BONDS', 'SHORT', 14340, 14420), # todo: check
# The June expires in a few days and I will switch to the Sept when
# available.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just bought gold @ $1364.20 with protective stop @ 1354.20 for
OpenTrade('GOLD', 'LONG', 136420, 135420),
# a 100 pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just set order to short Dow @ 15,280 on stop.  If filled, my
# protective stop will be at 15, 380 for a 100 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# IMPORTANT ANNOUNCEMENT

# The Tramline Traders website has been operating for almost a month and
# already, it is clear to Naomi and myself that we need to make major
# changes to our website and memberships. The format is too complicated
# and we need to set one blog in full on the home page.
# We shall be working on these changes very shortly, but in the
# meantime, we feel it is unfair to ask you to pay £97 for your second
# and subsequent months.  Therefore, we will keep the £17 monthly rate
# until we re-launch.  I have made the changes on our site.
# I will keep you updated about progress, but in the meantime, you will
# not see any change.
# Thank you for your loyalty, and I'm sure you will like the new site.
# Best Wishes,
# John BurfordTRAMLINE TRADERS
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have set order exiting my long Gold trade for A Account only @
# $1419.
# MoveStop('GOLD', 14190, ['A']), # TODO
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have moved protective stop to break even.
MoveStop('GOLD', 'BREAK EVEN'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just shorted Dow @ 15,255 with protective stop @ 15,480 for a
OpenTrade('DOW', 'SHORT', 15255, 15480),
# 125 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# I have a new FMT post.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# BARCLAYS
# I have just shorted Barclays @ 322 with protective stop @ 332 for a
# 100 pip risk.
# John
OpenTrade('BARCLAYS', 'SHORT', 3220, 3320),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have moved protective stop to break even @ 15,355.
MoveStop('DOW', 15355),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# My Weekly Wrap is now available here [1].
# Have a good weekend!
# John



# Links:
# ------
# [1] http://financialtradingstrategies.com/wpblog/
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# AUS/USDI have moved my protective stop on short AUS/USD in C Account
# to 0.9680
MoveStop('AUS/USD', 9680),
# DOWI am stopped at break-even 15,355
CloseTrade('DOW', 15355, 'ALL'),
# USD/JYI have exited my short trade USD/JY @ 102.00 for a small loss.
CloseTrade('USD/JY', 10200, 'ALL'),
# CAC40In error, posted a trade in Trading Record.  There was no Trade
# Alert.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# Having tech problems this morning, but today's Morning Call post is
# now online.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# GBP/USD
# I have just shorted GBP/USD @ 1.5065 with protective stop @ 1.51.65
# for a 100 pip risk
OpenTrade('GBP/USD', 'SHORT', 15065, 15165),
# EUR/USD
# I have just shorted EUR/USD @ 1.2875 with protective stop @ 1.2960 for
OpenTrade('EUR/USD', 'SHORT', 12875, 12960),
# a 85 pip risk
# FMT update soon.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just gone long gold @ $1381 with protective stop @ $1374 for a
OpenTrade('GOLD', 'LONG', 13810, 13740),
# 70 pip risk
# Will update FMT later.
# New post on US Dollar now online.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# The market did rally to the $1400 area, but then retreated back down
# to tramline.
# I do not like this!
# I have exited my long gold trade at $1382
CloseTrade('GOLD', 13820, 'ALL'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just shorted Dow @ 15,298 with protective stop @ 15,420 foR A
# 125 PIP RISK
OpenTrade('DOW', 'SHORT', 15298, 15420),
# FTSE
# I have just shorted FTSE @ 6648 with proetctive stop @ 6740 for  92
OpenTrade('FTSE', 'SHORT', 6648, 6740),
# PIP RISK
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# A very annoying market!  It is now moving up above the critical $1400
# level taking out many buy stops
# I have just gone long gold @ $1405 with protective stop @ $1385 for a
OpenTrade('GOLD', 'LONG', 14050, 13850),
# 200 pip risk, slightly higher than I normally like.
# Will have MC later this morning with my analysis and charts of Dow,
# FTSE and Gold.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# CAC-40
# I have just shorted CAC 40 @ 3,942 with protective stop @ 3980 for a
OpenTrade('CAC 40', 'SHORT', 3942, 3980),
# 38 pip risk.  And I bet three times normal because of small size.
# I have a feeling we will open weak on Monday in all stock indexes.
# Full charts and analysis in tomorrows WR.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3020 with protective stop @ 1.3070 for
OpenTrade('EUR/USD', 'SHORT', 13020, 13070),
# a 50 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS (30 YR)
# I have just bought Sept T-Bonds @ 140.80 with protective stop @ 139.80
OpenTrade('SEPT T-BONDS', 'LONG', 14080, 13980),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# Was going well and rebounded closer to my tramline.  
# I have exited the short EUR/USD @ 1.3020 at entry price.
CloseTrade('EUR/USD', 13020, 'ALL'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3050 with protective stop @ 1.3120 for
OpenTrade('EUR/USD', 'SHORT', 13050, 13120),
# a 70 pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS (30 YR)
# I have just gone long Sept T-Bonds @ 140.20 with protective stop @
# 139.50 for a 70 pip risk.
OpenTrade('SEPT T-BONDS', 'LONG', 14020, 13950),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just taken profit for A ACCOUNT only on my short Dow @ 15,000
CloseTrade('DOW', 15000, ['A']),
# FTSE
# I have just taken profit for A ACCOUNT only on my short FTSE @  6410
CloseTrade('FTSE', 6410, ['A']),
# SEPT T-BONDS
# I have moved my stop to break even @ 140.20
MoveStop('SEPT T-BONDS', 14020),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# FMT SUBSCRIPTIONS

# As you know, we are charging only £17 per month for FMT  - not £97.
#  This applies until we re-launch our site later this month.
# If you have not cancelled your original PayPal arrangement and
# re-applied with the amended payments, then please let Naomi know
# (through the Contact Us page) if you see a PayPal charge of £97 let
# her know and she will make arrangement for a refund of the £80
# difference.
# Also, I shall be away next Monday for a short break and will have no
# blog updates.  Back for early Tuesday.
# Regards,
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3225 with protective stop @ 1.3260 for
OpenTrade('EUR/USD', 'SHORT', 13225, 13260),
# a 55 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW AND FTSE
# I am moving protective stops on shorts to 15,298 and 6648 resp.
MoveStop('DOW', 15298),
MoveStop('FTSE', 6648),
# USD/JY
# I have just gone long USD/JY @ 97.20 with protective stop @ 96.20 for
OpenTrade('USD/JY', 'SHORT', 9720, 9620),
# a 100 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3250 with protective stop @ 1.3290 for
OpenTrade('EUR/USD', 'SHORT', 13250, 13290),
# a 40 pip risk
# GBP/USD
# I have just shorted GBP/USD @ 1.5530 with protective stop @ 1.5580 for
OpenTrade('GBP/USD', 'SHORT', 15530, 15580),
# a 50 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# FTSE
# I have taken profit for B ACCOUNT ONLY on my short FTSE @ 6,300
CloseTrade('FTSE', 6300, ['B']),
# BARCLAYS
# I have taken profit for A ACCOUNT ONLY on the first Barclays trade @
# 300
CloseTrade('BARCLAYS', 3000, ['A']), #todo: check which trade

# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just gone long Gold @ 1379 with protective stop @ 1372 for a 70
OpenTrade('GOLD', 'SHORT', 13790, 13720),
# pip risk.
# John 
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just shorted the Dow @ 15,125 with protective stop @ 15,225
OpenTrade('DOW', 'SHORT', 15125, 15225),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3325 with protective stop @ 1.3365 for
OpenTrade('EUR/USD', 'SHORT', 13325, 13365),
# a 40 pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS 30-YR
# I have just gone long Sept T-Bonds @ 139.60 with protective stop @
# 138.80 for an 80 pip risk.
OpenTrade('SEPT T-BONDS', 'LONG', 13960, 13860),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3320 with protective stop @ 1.3380 for
OpenTrade('EUR/USD', 'SHORT', 13320, 13380),
# a 60 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just exited my long trade at break-even 1380.
CloseTrade('GOLD', 13800, 'ALL'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have moved my stop on short Dow trade to break even @ 15,125
MoveStop('DOW', 15125),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just gone long gold @ 1386 with protective stop @ 1378 for an
OpenTrade('GOLD', 'SHORT', 13860, 13780),
# 80 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have just entered a buy stop @ 95.50 in USD/JY for a new position.
#  If filled, my protective sell stop will be @ 94.60 for a 90 pip
# risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# NIKKEI
# I have just gone long Rolling Nikkei @ 12,800 with protective stop @
# 12,700 for a 100 pip risk
OpenTrade('NIKKEI', 'LONG', 12800, 12700),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# I have moved protective stops on these trades to break-even:
# 1.  Long Sept T-Bonds to 139.60
MoveStop('SEPT T-BONDS', 13960),
# 2.  Long Gold to 1386
MoveStop('GOLD', 13860),
# I have also taken profit for C Account in short FTSE @ 6,335
CloseTrade('FTSE', 6335, ['C']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY

# I have cancelled my  order to go long USD/JY @ 95.50 stop and now I
# have gone long @ 95.00 with protective stop @ 93.95 for a 105 pip
OpenTrade('USD/JY', 'LONG', 9500, 9395),
# risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have just taken profit for A ACCOUNT ONLY on long USD/JY @ 97.95.
CloseTrade('USD/JY', 9795, ['A']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3190 with protective stop @ 1.3290 for
OpenTrade('EUR/USD', 'SHORT', 13190, 13290),
# a 100 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# FTSE
# I have just shorted FTSE @ 6,180 with protective stop @ 6,280 for a
OpenTrade('FTSE', 'SHORT', 6180, 6280),
# 100 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# I have just shorted Dow @ 14,770 with protective stop @ 14,950 for a
OpenTrade('DOW', 'SHORT', 14770, 14950),
# 180 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS 30 YR
# I gave just gone long Sept T-Bonds @ 136.00 with protective stop @
# 135.50 for a 50 pip risk.
OpenTrade('SEPT T-BONDS', 'LONG', 13600, 13550),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# 1.  I have just exited short Barclays for A ACCOUNT ON THE SECOND
# TRADE from June 6 @ 283
CloseTrade('BARCLAYS', 2830, ['A']), # todo find correct trade
# 2.  Also exited short Barclays for B ACCOUNT ON FIRST TRADE from May
# 23 @ 283
CloseTrade('BARCLAYS', 2830, ['B']),
# 3.  I have just exited long USD/JY for B Account @ 98.30
CloseTrade('USD/JY', 9830, ['B']),
# 4.  I have just gone long Gold @ 1,283 with protective stop @ 1,273
OpenTrade('GOLD', 'LONG', 1283, 1273),
# for a 100 pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS
# I have just gone long Sept T-Bonds @ 13420 with protective stop @
# 133.50 for a 70 pip risk.
OpenTrade('SEPT T-BONDS', 'LONG', 13420, 13350),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS
# I have taken profit on long Sept T-Bonds for A ACCOUNT @ 135.30 and
CloseTrade('SEPT T-BONDS', 13530, ['A']),
# moved stops for B and C Accounts to break even
MoveStop('SEPT T-BONDS', 'BREAK EVEN'),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# I have just shorted GBP/USD @ 1.5440 with protective stop @ 1.5480 for
OpenTrade('GBP/USD', 'SHORT', 15440, 15480),
# a 50 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS
# I have just gone long Sept T-Bonds @ 13445 with protective stop @
# 134.00 for a 45 pip risk.
OpenTrade('SEPT T-BONDS', 'LONG', 13445, 13400),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# GOLD
# I have just gone long Gold @ 1241 with protective stop @ 1231 for a
OpenTrade('GOLD', 'SHORT', 12410, 12310),
# 100 pip risk
# EUR/USD
# I have moved protective stop on short trade to break even @ 1.3190
MoveStop('EUR/USD', 13190),
# GBP/USD
# I have moved protective stop on short trade to break even @ 1.5440
MoveStop('GBP/USD', 15440),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# EUR/USD,  GBP/USD
# I have just taken profits for A Account on short EUR/USD @ 1.3030 and
# short GBP/USD @ 1.5320
CloseTrade('EUR/USD', 13030, ['A']),
CloseTrade('GBP/USD', 15320, ['A']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just taken profit for B ACCOUNT on short EUR/USD @ 1.3045.
CloseTrade('EUR/USD', 13045, ['B']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just exited for C Account my short EUR/USD @ 1.3070
CloseTrade('EUR/USD', 13070, ['C']),
# GBP/USD
# I have just exited for B Account my short GBP/USD @ 1.5250
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS
# I have just exited all long Sept T-Bonds for all accounts @ 135.50
CloseTrade('SEPT T-BONDS', 13550, 'ALL'),
# DOW
# I have just shorted Dow @ 15,000 with protective stop @ 15060 for 60
OpenTrade('DOW', 'SHORT', 15000, 15060),
# pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# I have just gone long GBP/USD @ 1.5245 with protective stop @ 1.5220
OpenTrade('GBP/USD', 'LONG', 15245, 15220),
# for a 25 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just gone long gold @ 1211 with protective stop @ 1198 for a
OpenTrade('GOLD', 'LONG', 12110, 11980),
# 130 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just taken profit for A ACCOUNT on long Gold @ 1246
CloseTrade('GOLD', 12460, ['A']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# I have just gone long GBP/USD @ 1.5210 with protective stop @ 1,5160
OpenTrade('GBP/USD', 'LONG', 15210, 15160),
# for a 50 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# BARCLAYS
# I have just taken profit for B ACCOUNT on short from June 8 trade @
# 285
CloseTrade('BARCLAYS', 2850, ['B']),
# This means I have only the two C Account positions open
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just taken profit for B ACCOUNT On long Gold @ $1254
CloseTrade('GOLD', 12540, ['B']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# We received your request for information from the Tramline Tradersascjones
# group.  Before we begin sending you the information you
# requested, we want to be certain we have your permission.



# -----------------------------------------------------------
# CONFIRM BY VISITING THE LINK BELOW:

# http://www.aweber.com/z/c/?yjxs7y03bxlb2dqbua2hp2db2tty036mg=861

# Click the link above to give us permission to send you 
# information.  It's fast and easy!  If you cannot click the 
# full URL above, please copy and paste it into your web 
# browser.

# -----------------------------------------------------------
# If you do not want to confirm, simply ignore this message. 

# Thank you,
# Tramline Traders

# Ash Cottage, Middle Hill, Broadway, Worcestershire WR12 7LA, UNITED KINGDOM

# Request generated by:
# IP: 95.144.120.44
# Date: July 2, 2013 13:13 EDT
# URL: https://www.aweber.com/users/leads/add?success=1
# ----------------------------------------------------
# ----------------------------------------------------
# Tramline Traders

# .
# FOLLOW MY TRADES



# You have seen how I use my unique Tramline Trading methods not only
# to extract profits from the winners, but also to minimize losses on
# the losing trades.

#  The correct attitude to achieving success is to ride the winners
# and cut the losers.  For many, this is easier said than done.  The
# problem is this: there is no way on earth that can identify a trade
# as a winner or a loser ahead of time!  You have to play the
# percentages.

# My A-B-C Strategy

# But with my simple but effective system for setting up three
# accounts in one, it is as easy as ABC!   Here's how:

#           'A' Account - used for short-term moves (hours and days)

#           'B' Account - used for medium-term moves (days and weeks)

#           'C' Account - used for long-term moves (weeks and months)

#  And I don't need to set up three separate accounts with my
# provider - I just make one bet and peel off the trades one by one
# as targets are hit.

#  Here is an example of this system in use:

# This is the Aussie dollar which I shorted in May

# .On 5 May, I shorted the AUS/USD in the 102.50 area on a major
# tramline break.  I placed equal bets in the three accounts.  I
# placed my protective stop at 50 pips above entry, giving me a very
# low-risk trade.
#  FINDING LOW-RISK ENTRIES IS ESSENTIAL FOR LONG-TERM PROFITS!

#  And as the market went my way, I took a 100 pip profit for A
# Account on an oversold momentum/tramline hit.  And I still had the
# B and C trades working.

#  Then, as the market declined further, I took a 300 pip profit for
# B Account on a Fibonacci retrace.  And I still had the C Account
# trade open.

#  As I write, I have taken 400 pips for A and B Accounts off the
# table, and have an open gain of 600 pips in the C Account.

#  The minimum size bet is three pips - one pip in each of the three
# accounts with the initial protective stop 50 pips away for all
# three.

#  That is a potential profit of 1000 pips on a 3 pip spread bet, and
# at only £5 per pip, that is a £5,000 potential gain (remember, I
# still have the C Account trade working, so this gain has not been
# realized in this account).

#  Of course, these trades do not come along every day, but to take
# advantage, I need to keep my eyes open for them.

# Now, I believe my service could be of great benefit to traders of
# all levels, from the novice to the much more experienced.
#  It can teach you what clues to look for - and help you with the
# discipline required to put my methods into practice.

#  The novice trader in particular will gain valuable insights into
# the anatomy of a trade, from the initial analysis using tramlines,
# Fibonacci levels and Elliott Waves, to the correct use of money
# management discipline.

#  Most traders lose money not because they are lousy analysts!  They
# lose because they are unable to bring sufficient discipline into
# their risk management - and many take profits too early.

#  My A-B-C strategy is a wonderful way to manage market risk while
# riding a potential whale!

#  And if you subscribe, you will receive Trade Alerts when I exit a
# trade for any one of the accounts.

# YOU WILL RECEIVE MY TRADE ALERTS BY EMAIL AND NOW YOU HAVE THE
# OPTION OF RECEIVING THEM BY SMS TEXT MESSAGE.



# Sincerely


# John Burford



# You get all of this for only £47 per month!

#  So I invite you to join the Tramline Traders - and kick your
# performance into a higher gear - as easily as A B C

# for John's Trade Alerts.

# Click to review our privacy policy. [
# http://clicks.aweber.com/y/ct/?l=NJAfg&m=3_NWefqe8.OO1zG&b=N7XW9KtWSmpNgRePmLp.qw ]

# If you would no longer like to receive emails from us please use
# the unsubscribe link below.

# Ash Cottage, Middle Hill, Broadway, Worcestershire WR12 7LA, UNITED KINGDOM

# To unsubscribe or change subscriber options visit:
# http://www.aweber.com/z/r/?TOyMjBxs7LSsLGwcDIyMjLRmtIzsbJzMLEws
# ----------------------------------------------------
# ----------------------------------------------------
# I have a new Follow my Trade post on the website on gold.

# TRADE ALERT
# GOLD
# I have a long trade working in C ACCOUNT from $1211 June 28 and I have
# now exited this position @ $1285.0
CloseTrade('GOLD', 12850, ['C']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have just exited for C ACCOUNT my long USD/JY trade taken at 95.00
# at 99.00
CloseTrade('USD/JY', 9500, ['C']),

# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS
# I have just shorted Sept T-Bonds @ 134.80 with protective stop @
# 135.40 for A 60 PIP RISK.
OpenTrade('SEPT T-BONDS', 'SHORT', 13480, 13540),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just shorted Dow @ 15,430 with protective stop @ 15,490 for a
# 60 pip risk
OpenTrade('DOW', 'SHORT', 15430, 15490),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS
# I have moved my stop to break even on short Sept T-Bonds to 134.80
MoveStop('SEPT T-BONDS', 13480),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have just shorted USD/JY @ 99.40 with protective stop @ 99.75 for a
# 35 pip risk.
OpenTrade('USD/JY', 'SHORT', 9940, 9975),
# FTSE
# I have just shorted FTSE @ 6570 with protective stop @ 6610 for a 40
OpenTrade('FTSE', 'SHORT', 6570, 6610),
# pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3100 with protective stop @ 1.3195 for
OpenTrade('EUR/USD', 'SHORT', 13100, 13195),
# a 100 pip risk.
# GOLD
# I have just shorted Gold @ $1282 with protective stop @ $1302 for a
OpenTrade('GOLD', 'SHORT', 12820, 13020),
# 200 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# SEPT T-BONDS
# I have just shorted Sept T-Bonds @ 135.10 with protective stop @
# 135.70 for a 60 pip risk.
OpenTrade('SEPT T-BONDS', 'SHORT', 13510, 13570),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# NASDAQ (0.1) ROLLING
# I have just shorted Nasdaq @ 3050 with protective stop @ 3060
# DOW
OpenTrade('NASDAQ', 'SHORT', 30500, 30600),
# I have just shorted Dow @ 15,580 with protective stop @ 15,610
OpenTrade('DOW', 'SHORT', 15580, 15610),
# John

# ----------------------------------------------------
# ----------------------------------------------------
# I have been out of the office for most of today and consequently
# missed the big declines in many of my markets.
# It does appear we have a turn in gold (suggested in MC today), US
# stocks (suggested in MW Trader emails), currencies, Treasuries.  The
# European stock indexes are holding up much better.
# I will be looking to position short again on rallies from here.
#  There is plenty of time to climb aboard gold and the Dow, Nasdaq, as
# I remain convinced the declines will be historic.
# If you have taken the opportunity to go short, then congratulations.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted GBP/USD @ 1.1.5320 with protective stop @ 1.1.5420
OpenTrade('GBP/USD', 'SHORT', 115320, 115420),
# for a 100 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# FTSE
# I have just shorted FTSE @ 6,595 with protective stop @ 6,640 for a 45
OpenTrade('FTSE', 'SHORT', 6595, 6640),
# pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just shorted Dow @ 15,520 with protective stop @ 15,580 for a
OpenTrade('DOW', 'SHORT', 15520, 15580),
# 60 pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/CHF (SWISSIE)
# I have just gone long USD/CHF @ 0.9290 with protective stop @ 0.9250
# for a 40 pip risk.
OpenTrade('USD/CHF', 'LONG', 9290, 9250),
# GBP/USD
# I have just gone short GBP/USD @ 1.5380 with protective stop @
#  1.5410 for a 30 pip risk.
OpenTrade('GBP/USD', 'SHORT', 15380, 15410),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3265 with protective stop @ 1.3310 for
OpenTrade('EUR/USD', 'SHORT', 13265, 13310),
# a 45 pip risk
# GBP/USD
# I have just re-instated short GBP/USD @ 1.5380 with protective stop @
# 1.5420 for a 40 pip risk
OpenTrade('GBP/USD', 'SHORT', 15380, 15420),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/CAD (CANADIAN DOLLAR)

# I have just gone long USD/CAD @ 1.0280 with protective stop @ 1.0240
# for a 40 pip risk.
# John
OpenTrade('USD/CAD', 'LONG', 10280, 10240),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# NIKKEI
# I have just gone long Nikkei 225 (USD) @ 13.700 with protective stop @
# 13,620 for 80 pip risk.
OpenTrade('NIKKEI', 'LONG', 13700, 13620),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# I have just covered for A ACCOUNT my short GBP/USD @ 1.5200
CloseTrade('GBP/USD', 15200, ['A']),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLDi have just shorted gold @ $1,310 with protective stop @ $1,325
OpenTrade('GOLD', 'SHORT', 13100, 13250),
# for a 150 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/CHF (SWISSIE)
# I have just gone long USD/CHF @ 0.9287 with protective stop @ 0.9240
# for a 47 pip risk.
# John
OpenTrade('USD/CHF', 'LONG', 9287, 9240),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have just shorted Dow @15,520 with protective stop @ 15,590 for a 70
OpenTrade('DOW', 'SHORT', 15520, 15590),
# pip risk.
# John 
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# GBP/USD
# I have just shorted GBP/USD @ 1.5520 with protective stop @ 1.5570 for
OpenTrade('GBP/USD', 'SHORT', 15520, 15570),
# a 50 pip risk
# DOW
# I have just shorted Dow @ 15,400 with protective stop @ 15,500 for a
OpenTrade('DOW', 'SHORT', 15400, 15500),
# 100 pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# DAX  30 (GERMAN STOCK INDEX)
# I have just shorted DAX @ 8,258 with protective stop @ 8330 for 72 pip
# risk
OpenTrade('DAX', 'SHORT', 8258, 8330),
# NASDAQ
# I have just shorted Nasdaq @ 3,100 with protective stop @ 3,130 for
OpenTrade('NASDAQ', 'SHORT', 3100, 3130),
# 130 pip risk
# The odds are very high we are in large third waves down in all
# indexes.  That is why gold has jumped overnight.  The downside
# beckons.
# More on MC later this morning.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# ALCOA
# I have just gone long Alcoa @ 8.20 with protective stop @ 7.90.
OpenTrade('ALCOA', 'SHORT', 820, 790),
# I have some excellent tramlines working and am returning to this
# market after a break where it has been forming a bottom, I believe.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just shorted Gold @ 1,336 with protective stop @ 1,346 for a
# 100 pip risk
# John
OpenTrade('GOLD', 'SHORT', 13360, 13460),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT

# SEPT T-BONDS
# I have just gone long Sept T-Bonds @ 132.60 with protective stop @
# 131.60 for 100 pip risk
OpenTrade('SEPT T-BONDS', 'LONG', 13260, 13160),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/CAD
# I have just shorted USD/CAD @ 1.0340 with protective stop @ 1.0390 for
OpenTrade('USD/CAD', 'SHORT', 10340, 10390),
# 50 pip risk.
# I am looking for break of 1.02.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# I have exited for A ACCOUNT short Dow @ 14,855 on the first trade
CloseTrade('DOW', 14855, ['A']),
# @15,520 on 6 Aug.
# Profit of 665 pips in three weeks.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# I have just shorted GBP/USD @ 1.5580 with protective stop @ 1.5630 for
OpenTrade('GBP/USD', 'SHORT', 15580, 15630),
# 50 pip risk
# Have a Fib 50% retrace of last wave down and on C wave of an A-B-C up.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DAX
# I have just shorted DAX (German stock index) @ 8245 with protective
# stop @ 8290 for 45 pip risk.
OpenTrade('DAX', 'SHORT', 8245, 8290),
# It has made a 50% Fib retrace of the decline off the 8430 high and
# into severe resistance.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have shorted USD/JY @ 99.45 with protective stop @ 99.90 for 45 pip
OpenTrade('USD/JY', 'SHORT', 9945, 9990),
# risk
# I have been out of the office this afternoon and could have got a
# better entry!
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DEC T-BONDS 30-YR
# I have just shorted Dec T-Bonds @ 130.16 with protective stop @ 130.60
OpenTrade('DEC T-BONDS', 'SHORT', 13016, 13060),
# for 34 pip risk
# ______________________________
# I have moved my protective stops to break-even on:
# Short DAX (8245)
MoveStop('DAX', 8245),
# Short EUR/USD (1.3340)
MoveStop('EUR/USD', 13340),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# TESLA MOTORS

# This is a US share and has seen an exponential rally this year.  It
# is a bubble (their electric cars cost $100,000!) and there is a cult
# surrounding the CEO - a Mr Musk.  This is a classic bubble situation.
# When the bubble bursts, it will a spectacular show.
# I am seeing signs today that we could be near - a tramline has been
# broken.
# TRADE  I have just shorted TESLA Motors @ 165.90 with protective stop
# @ 170.00
OpenTrade('TESLA', 'SHORT', 16590, 17000),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# I have just shorted GBP/USD @ 1.5640 with protective stop @ 1.5690 for
OpenTrade('USD/JY', 'SHORT', 9970, 10030),
# 50 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# IMPORTANT ANNOUNCEMENT

# We are moving our payments system to another PayPal account and ask
# your cooperation urgently.
# WOULD YOU KINDLY CANCEL YOUR EXISTING MANDATE WITH US TODAY AND
# RE-REGISTER IN THE SAME WAY AS BEFORE. THIS WILL TAKE YOU INTO OUR NEW
# PAYPAL ACCOUNT.
# I realise many members have only recently renewed and I will undertake
# to refund any unused portion of your current membership fee if you
# care to apply to me.
# I apologise for any inconvenience and once again, please treat this
# with urgency.  Thank you.
# Also, the new website is almost done and I will make announcement on
# this shortly.  
# Kind Regards,
# JohnTRAMLINE TRADERS
# ----------------------------------------------------
# ----------------------------------------------------
# Dear FMT Member,
# We are having problems with our new paypal account and you will not be
# able to renew just yet.  We hope to have it fixed very soon. 
# Still go ahead and cancel your existing subscription, as I asked in my
# earlier email.
# Meanwhile, be assured you will still receive my Trade Alerts
# uninterrupted.
# Regards,
# JohnTRAMLINE TRADERS
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have just shorted USD/JY @ 99.70 with protective stop @ 100.30 for a
OpenTrade('USD/JY', 'SHORT', 9970, 10030),
# 60 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT

# DEC T-BONDS
# I have just taken profit on short Dec T-Bonds for A Account @ 128.70.
CloseTrade('DEC T-BONDS', 12870, ['A']),
#  B and C Account trades are still open.
# The US Unemployment Rate data is out later today and we should see a
# volatile market, especially because the market is heavily short
# John
# ----------------------------------------------------
# ----------------------------------------------------
# Dear FMT Subscriber,
# PAYPAL IS NOW  WORKING

# I am pleased to announce we have de-bugged our payments platform and
# you can now go ahead and cancel your existing membership and renew on
# the website tramlinetraders.com.
# As I stated in my first email, if you have a major unused portion of
# your old membership, drop me a line and I will refund that part.
# Happy trading!
# JohnTRAMLINE TRADERS
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# OCT CRUDE OIL US
# I have just shorted Oct US Crude @ 109.05 with protective stop @
# 109.50 for 45 pip risk.
OpenTrade('OCT US CRUDE', 'SHORT', 10905, 10950),
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DEC T-BONDS
# I have just taken profit for B Account on short Dec T-Bonds @ 129.40.
CloseTrade('DEC T-BONDS', 12940, ['B']),
#  C Account trade still open.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DAX
# I have just shorted DAX @ 8282 with protective stop @ 8325 for a 43
# pip risk.
OpenTrade('DAX', 'SHORT', 8282, 8325),
# Have hit a meeting of  62% Fib retrace, an upper tramline and wave C
# = wave A here.  This should be solid resistance.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DEC T-BONDS
# I have just exited my short Dec T-Bonds for C Account @ 128.70.
# John
CloseTrade('DEC T-BONDS', 12880, ['C']),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DEC T-BONDS 30-YR
# I have just gone long Dec T-Bonds @ 128.80 with protective stop @
# 128.40 for 40 pip risk.
OpenTrade('DEC T-BONDS', 'LONG', 12880, 12840),
# See today's MC.  Market has dropped to Fib 87% of rally off 6 Sep low
# into support.  I am looking for at least 200-300 pips.  I took
# profit on short trade for C Account earlier.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# TESLA MOTORS (US SHARE)
# I have just shorted Tesla @ 165.10 with protective stop @ 169.
# John
OpenTrade('TESLA', 'SHORT', 16510, 169),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# ALCOA
# I am warming to ALCOA again (see previous post)  It is nudging big
# downtrend line and with Dow etc in melt-up, Alcoa should follow.
#  When we do get a turn down in the major indexes, Alcoa should hold
# up well as it is already on the floor and is totally unloved and short
# interest must be small or even non-existent (I must check).
# I HAVE JUST GONE LONG ALCOA @ 8.10 WITH STOP @ 7.70 FOR A SWING TRADE.
OpenTrade('ALCOA', 'LONG', 810, 770),
# I have also been accumulating the shares as an investment (long term).
# See previous posts for rationale and charts.

# The Dow is running towards the Fib 78% retrace at the 15,320 area.
#  Remember, I have been commenting for months that after a decline,
# the retrace is usually very deep - at the 78% level or even above.
#  This is wave 2 and such a deep retrace is entirely in chacter.
# John 
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# Has hit my target at 1.5800 (slight overshoot of Fib 62% retrace and
# chart resistance from November).  Severe neg mom div on daily.
# I have just shorted GBP/USD @ 1.5802 with protective stop @ 1.5860
OpenTrade('GBP/USD', 'SHORT', 15802, 15860),
# EUR/USD
# And euro has hit target (62% Fib) and a neg mom div on hourly.
# I have just shorted EUR/USD @ 1.3298 with protective stop @ 1.3330.
OpenTrade('EUR/USD', 'SHORT', 13298, 13330),
# USD/JY
# Has done an A-B-C dip today and is looking bullish
# I have just bought USD/JY @ 100.05 with protective stop @ 99.60.
OpenTrade('USD/JY', 'LONG', 10005, 9960),
# DOW
# By one measure, the Dow @ 15,270 has reached a major target, but lies
# between two Fibs.  It may have done enough to complete the rally.  I
# shall be watching the FTSE which may be on the brink, so stay tuned.
# John

# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERTS
# USD/JY
# I was stopped out of long USD/JY trade, but
CloseTrade('USD/JY', 'STOP', 'ALL'),
# I have just gone long USD/JY @ 99.40 with protective stop @ 98.90 for
OpenTrade('USD/JY', 'LONG', 9940, 9890),
# 50 pip risk.
# Have a Fib 62% retrace and rests on support.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# See analysis this morning call.  Have just poked above tramline.
# I have just gone long Gold @ 1316 with protective stop @ 1296 for 200
# pip risk
# John
OpenTrade('GOLD', 'LONG', 13160, 12960),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# In the past few moments, the Dow has poked up to 15,380 - my wave 5
# that I was looking for (see today's MC and MW Trader email.  Now if
# this high holds, we will have a huge neg mom div on the hourly.
# I have just shorted Dow @ 15,360 with protective stop @ 15,400 for 40
# pip risk.
# John
OpenTrade('DOW', 'SHORT', 15360, 15400),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DEC T-BONDS
# I have just taken profits for A Account on long Dec T-Bonds @ 131.24,
CloseTrade('DEC T-BONDS', 13124, ['A']),
# leaving B and C trades open.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# I was short the Dow from August.  On the rally back up, I have exited
# these trades at either break-even or for small profit
# That was disappointing, but I believe there are riches just around the
# corner.
# If you are trading short the Dow, I hope you have done something
# similar.
# The big day is tomorrow - at around 7 pm UK time, and I have a trade
# set-up which I will place ahead of time as a stop order.
# Tomorrow late could be very wild, and getting a fill in a fast market
# could be impossible.  By placing a stop entry order, I will be
# assured of a decent fill, if my price is hit.  If it isn't, no harm
# done.
# NASDAQ
# I will enter an order to short the Nasdaq @ 3160 on stop.  If filled,
# I will enter protective stop @ 3190.
# Full analysis on the main website in FMT section later today.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# The news is out and the Fed are not changing a thing - against most
# 'experts' expectations for at least a $10 billion taper.
# Be that as it may, this places my gold and T-Bond positions in good
# shape as both have rallied strongly. Remember, both have suffered from
# extreme bearish sentiment recently and are due for a good pop.
# And stocks have also rallied  - so my open order to short Nasdaq went
# unfilled.  I have cancelled that order, so no harm done.
# In today's MW Trader email I had a 1.61 target for GBP/USD and we have
# come within 20 pips as I write.  I shall be watching the action for
# signs of a top.
# But thank you Fed, for juicing my gold and T-Bond trades!
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just taken profit on long Gold for A Account @ 1.363.  My B
# and C trades still open and have moved stop on them from $1286 to
# $1330.
CloseTrade('GOLD', 13630, ['A']),
MoveStop('GOLD', 13300),
# It has hit Fib 50% retrace and meeting of two tramlines (charts later
# today in MC post)

# GBP/USD
# I have just shorted GBP/USD @ 1.6125 with protective stop @ 1.6175.
OpenTrade('GBP/USD', 'SHORT', 16125, 16175),
# It has made an overshoot of upper tramline and hit targets set
# yesterday in my MW Trader email.

# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# I have just exited for B account my long Gold trade @ $1362.
CloseTrade('GOLD', 13620, ['B']),
# The Dow and Nasdaq seem to be backing off their upper tramlines and I
# may have a trade soon.

# John
# ----------------------------------------------------
# ----------------------------------------------------
# Dear FMT Subscriber,

# Later today, we are switching into the new website format - keeping
# the tramlinetraders.com URL.  I will post regular blogs on the home
# page, and you are welcome to check in regularly.
# For the past few weeks while we have been wrestling with building the
# new site, I have kept the FMT subscription at a very nominal level at
# £17 a month to help compensate you for the upheaval.
# The good news is that I will continue to offer FMT, but at a more
# realistic $47 per month.  I'm sure you recognise what tremendous
# value this is as I am confident  you have picked up some great
# trading ideas already.  And there are lots more to come!.
# I WILL ASK YOU TO CANCEL YOUR EXISTING SUBSCRIPTION AND RE-SUBSCRIBE
# IN THE NEW FORMAT (FROM SATURDAY SHOULD BE FINE).  
# After that, if you believe you have paid for a significant unused
# portion of the existing period and would like a refund, then get back
# to me giving your bank details and I will arrange a refund of that
# portion.
# I am excited by the change and once again, many thanks for your
# patience during this difficult period.  I hope you like the new
# format!
# Best Wishes,
# John BurfordTRAMLINE TRADERS
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# See this morning's MC.  A budding upside breakout which could reach
# over 100
# I have just gone long USD/JY @ 99.45 with protective stop @ 99.20 for
OpenTrade('USD/JY', 'LONG', 9945, 9920),
# a 25 pip risk
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GBP/USD
# I have just taken profit for A Account on short GBP/USD @ 1.600.
CloseTrade('GBP/USD', 1600, ['A']),
# It has hit a lower tramline support.  Will keep B and C trades open
# with stops at break even.

# I have just posted a gold study on the main website.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# GOLD
# Has fallen rapidly to major support in the 1335 area,  That is also a
# 50% Fib retrace of this week's rally.
# I have just gone long gold @ 1335 with protective stop @ 1325 for 100
# pip risk.
# John
OpenTrade('GOLD', 'LONG', 13350, 13250),
# ----------------------------------------------------
# ----------------------------------------------------
# RE: TRAMLINE TRADERS WEBSITE
# We are having problems with the switch-over to the new site and some
# readers are not able to view it.
# I am working on it as fast as I can and hope to have it up and running
# very soon.
# If the problems are not fixed soon, I shall post Morning Calls on my
# alternative site, so keep checking there.
# www.financialtradingstrategies.com/wpblog
# Meanwhile, my FMT service is not interrupted.
# I have a MW Trader post on the Dow today and the Equinox effect.
#  Hope you enjoy.
# Regards,
# JohnTRAMLINE TRADERS
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# NASDAQ 100
# I have just shorted Nasdaq @ 3218 with protective stop @ 3225 for 70
OpenTrade('NASDAQ', 'SHORT', 3218, 3225),
# pip risk
# Big move down from Friday and have a Fib 38% retrace into resistance
# overhead.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# THE NEW SITE IS UP AND RUNNING

# DOW
# I have just gone long Dow @ 15,400 with protective stop @ 15,370 for
# 30 pip risk.
# John
OpenTrade('DOW', 'LONG', 15400, 15370),
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DEC T-BONDS
# Have just hit my main target at 133.
# TRADE  I have just taken profit for B Account on long Dec T-Bond from
# 128.80 @ 132.92.
CloseTrade('DEC T-BOND', 13292, ['B']),
# My C Account trade is still open.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# Dear FMT Subscriber,
# PLEASE CANCEL EXISTING FMT SUBSCRIPTIONS BY FRIDAY 27 SEPTEMBER
# AND RENEW UNDER THE NEW SERVICE.. THANK YOU.

# Our new format website is now live and the old FMT arrangement is
# shutting down on Friday 27 September.
# All Trade Alerts after 27 September will be sent to current
# subscribers only.
# If you believe you have a large unused portion of your current month's
# fee of £17, do get in touch with me and I will arrange a refund for
# the unused portion.
# With Best Wishes,
# John BurfordTRAMLINE TRADERS
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# USD/JY
# I have just gone long USD/JY @ 98.60 with protective stop @ 98.30 for
# a 30 pip risk.
OpenTrade('USD/JY', 'LONG', 9860, 9830),
# I have been waiting for a low-risk entry and market has fallen ot the
# Fib 62% retrace.  First target is 99.20.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DOW
# With five down and a pos mom div - and the big gap now closed, stocks
# are due a good rebound in an A-B-C of over 100 pips.
# I have just gone long Dow @ 15,360 with protective stop @ 15,315 for a
OpenTrade('DOW', 'SHORT', 15360, 15315),
# 45 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# DEC T-BONDS

# I have just taken profit for C Account on long Dec T-Bonds @ 132.00.
CloseTrade('DEC T-BONDS', 13200, ['C']),
# I am now flat the bonds.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TRADE ALERT
# EUR/USD
# I have just shorted EUR/USD @ 1.3490 with protective stop @ 1.3540 for
OpenTrade('EUR/USD', 'SHORT', 13490, 13540)
# 50 pip risk.
# John
# ----------------------------------------------------
# ----------------------------------------------------
# TODAY IS SWITCH-OVER DAY
# If you have not already done so, please cancel your old Paypal
# arrangement with us today and sign in again using the new platform.
# If you do not renew, you will cease to receive my Trade Alerts.
# Many thanks for your cooperation.
# We have had a few annoying stop-outs recently - in addition to the big
# gains in T-Bonds.  This weekend could see volatility expand as
# political deadlock in US Congress looms.  A positive outcome should
# send stocks soaring.  But that is a gamble too far for me!  I shall
# watch and wait for now.
# JohnTRAMLINE TRADERS
# ----------------------------------------------------
]