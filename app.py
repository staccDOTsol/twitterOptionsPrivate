import requests

import csv

from get_all_tickers import get_tickers as gt

import investpy

tickers = gt.get_tickers()
df = investpy.etfs.get_etfs()
for index, row in df.iterrows():
    tickers.append(row['symbol'])
    

r = requests.get("https://spreadsheets.google.com/feeds/list/1Hq_yLJEXv5UmhadGm4b4Qm8BlXaSAupsWy696gb-gJw/od6/public/basic?alt=json").json()
for e in r['feed']['entry']:
	s = e['content']['$t']
	if ', _cpzh4: ' in s:
		buy = s.split(', _cpzh4: ')[0]
		sell = s.split(', _cpzh4: ')[1]
	else:
		buy = ''
		sell = s.replace('_cpzh4: ', '')
	if len(buy.split('ALERT:')) > 1:
		buys = buy.split('ALERT:')[1].split(' ')
	else:
		buys = buy.split(' ')

	if len(sell.split('ALERT:')) > 1:
		sells = sell.split('ALERT:')[1].split(' ')
	else:
		sells = sell.split(' ')
	buyw = ""
	

	if len(buys) <= 1:
		buyw = 'No buy text for this line!'
	else:
		for s in buys:
			if s in tickers:
				if len(s) > len(buyw):
					buyw = s
	sellw = ""
	for s in sells:
		if s in tickers:
			if len(s) > len(sellw):
				sellw = s

	print('buy ticker: ' + buyw + ' and buy string: ' + buy)

	print('sell ticker: ' + sellw + ' and sell string: ' + sell)
	#print('buy: ' + buy)
	#print('sell: ' + sell)	