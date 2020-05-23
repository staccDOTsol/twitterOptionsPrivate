import requests

import tweepy
import csv

from get_all_tickers import get_tickers as gt

import investpy

def dotweets(public_tweets):
    for tweet in public_tweets:
        max_id = tweet.id
        s = tweet.text
        sell = None
        buy = None
        sells = ""
        buys = ""
        if 'buy' in s.lower() or 'add' in s.lower() or 'in' in s.lower() or 'bought' in s.lower():
            buy = s
        elif 'sell' in s.lower() or 'out' in s.lower() or 'sold' in s.lower():
            sell = s
        
        
        if buy is not None:

            if len(buy.split('ALERT:')) > 1:
                buys = buy.split('ALERT:')[1].split(' ')
            else:
                buys = buy.split(' ')
        if sell is not None:
            if len(sell.split('ALERT:')) > 1:
                sells = sell.split('ALERT:')[1].split(' ')
            else:
                sells = sell.split(' ')
        buyw = ""
        
        if len(buys) <= 1:
            buyw = 'No buy text for this tweet!'
        else:
            for s in buys:
                if s in tickers:
                    if len(s) > len(buyw):
                        buyw = s
        sellw = ""
        if len(sells) <= 1:
            sellw = 'No sell text for this tweet!'
        else:
            for s in sells:
                if s in tickers:
                    if len(s) > len(sellw):
                        sellw = s
        if buy is not None:
            print('buy ticker: ' + buyw + ' and buy string: ' + buy)
        if sell is not None:
            print('sell ticker: ' + sellw + ' and sell string: ' + sell)
        #print('buy: ' + buy)
        #print('sell: ' + sell)    
        public_tweets = api.user_timeline({"screen_name": 'ducksquadpicks', "since_id": None, "max_id": max_id, "count": 50})
    dotweets(public_tweets)

tickers = gt.get_tickers()
df = investpy.etfs.get_etfs()
for index, row in df.iterrows():
    tickers.append(row['symbol'])


auth = tweepy.OAuthHandler('XVKyhUWhqDUcXsyl9uFnKcJ4u', 'viqbMU2IWbX8pcSqaEA7RaHyL6ua9256Ffs9bVD2PXc0LHPdL4')
auth.set_access_token('1024548186478637057-nYmeXy3nep57u499lXqz3aSYYjHgwk', 'mE385YuKr0rvngSXpoevDbRWv2vZu0MqiGegjjBSjZogb')

api = tweepy.API(auth)

public_tweets = api.user_timeline({"screen_name": 'ducksquadpicks', "since_id": None, "max_id": None, "count": 50})
dotweets(public_tweets)
