import requests

import tweepy
import csv

from get_all_tickers import get_tickers as gt

import investpy
with open("test.csv", "w") as myfile:
    myfile.write("Date,Symbol,Signal\n")
def dotweets(public_tweets):
    print('dotweets')
    for tweet in public_tweets:
        max_id = tweet.id
        #print(max_id)
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
            #else:
                #buys = buy.split(' ')
        if sell is not None:
            if len(sell.split('ALERT:')) > 1:
                sells = sell.split('ALERT:')[1].split(' ')
           # else:
                #sells = sell.split(' ')
        buyw = ""
        
        if len(buys) <= 1:
            buyw = ''
        else:
            for s in buys:
                if s in tickers:
                    if len(s) > len(buyw):
                        if len(s) > 1 and not s.isnumeric():
                            buyw = s
        sellw = ""
        if len(sells) <= 1:
            sellw = ''
        else:
            for s in sells:
                if s in tickers:
                    if len(s) > len(sellw):
                        if len(s) > 1 and not s.isnumeric():
                            sellw = s
        if buy is not None and len(buyw) > 0:
            with open("test.csv", "a") as myfile:
                print(buy)
                myfile.write(str(tweet.created_at)+','+buyw+',C\n')

            #print('buy ticker: ' + buyw + ' and buy string: ' + buy)
        elif sell is not None and len(sellw) > 0:
            with open("test.csv", "a") as myfile:
                print(sell)
                myfile.write(str(tweet.created_at)+','+sellw+',P\n')
        #else:
            #print(s)
            #print('sell ticker: ' + sellw + ' and sell string: ' + sell)
        #print('buy: ' + buy)
        #print('sell: ' + sell)    

    public_tweets = api.user_timeline(screen_name = 'duckingmoney', max_id = max_id, count = 100)
    print('ducksquadpicks', None, max_id)   
    if (len(public_tweets) > 5):
        dotweets(public_tweets)

tickers = gt.get_tickers()
df = investpy.etfs.get_etfs()
for index, row in df.iterrows():
    tickers.append(row['symbol'])


auth = tweepy.OAuthHandler('XVKyhUWhqDUcXsyl9uFnKcJ4u', 'viqbMU2IWbX8pcSqaEA7RaHyL6ua9256Ffs9bVD2PXc0LHPdL4')
auth.set_access_token('1024548186478637057-nYmeXy3nep57u499lXqz3aSYYjHgwk', 'mE385YuKr0rvngSXpoevDbRWv2vZu0MqiGegjjBSjZogb')

api = tweepy.API(auth)

public_tweets = api.user_timeline(screen_name = 'ducksquadpicks', count = 100)
dotweets(public_tweets)
