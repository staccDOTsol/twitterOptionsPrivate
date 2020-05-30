import requests

import tweepy
import csv

from get_all_tickers import get_tickers as gt

import investpy
with open("test.csv", "w") as myfile:
    myfile.write("Date,Direction,P/C,Ticker,Strike,Price,Expiry\n")
def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

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
        none = ""
        if 'buy' in s.lower() or 'add' in s.lower()  or 'added' in s.lower() or 'in' in s.lower() or 'bought' in s.lower():
            buy = s
            
        elif 'sell' in s.lower() or 'out' in s.lower() or 'sold' in s.lower():
            sell = s
        
        
        if buy is not None:

            if len(buy.split('NEW ALERT:')) > 1:
                buys = buy.split('NEW ALERT:')[1].split(' ')
                print(s)
            #else:
                #buys = buy.split(' ')
        elif sell is None:
            if len(s.split('NEW ALERT:')) > 1:
                none = s.split('NEW ALERT:')[1].split(' ')
                print(s)
        if sell is not None:
            if len(sell.split('NEW ALERT:')) > 1:
                sells = sell.split('NEW ALERT:')[1].split(' ')
                print(s)
        elif buy is None:
            if len(s.split('NEW ALERT:')) > 1:
                none = s.split('NEW ALERT:')[1].split(' ')
                print(s)
                #sells = sell.split(' ')
        pocs = []
        buyw = []
        strikes = []
        expiries = ""
        prices = []
        nonew = []
        if len(none) <= 1:
            nonew = []
        else:
            olds = ""
            for s in none:
                if s in tickers:
                    if len(s) > len(nonew):
                        if len(s) > 1 and not isfloat(s):
                            nonew.append(s)
                if isfloat(olds) and s == 'C':
                    pocs.append('C')
                    strikes.append(olds)
                if isfloat(olds) and s == 'P':
                    pocs.append('P')
                    strikes.append(olds)
                if '/' in s:
                    expiries = (s)
                if 'next' in olds and 'week' in s:
                    expiries = 'next week' 
                if 'this' in olds and 'week' in s:
                    expiries = 'this week' 
                if 'at' in olds and isfloat(s):
                    prices.append(s)
                olds = s
                
                
            while len(prices) < len(nonew) or len(strikes) < len(nonew) or len(pocs) < len(nonew):
                if len(prices) < len(nonew):
                    prices.append('')

                if len(strikes) < len(nonew):
                    strikes.append('')
                if len(pocs) < len(nonew):
                    pocs.append('')
        if len(buys) <= 1:
            buyw = []
        else:
            olds = ""
            for s in buys:
                if s in tickers:
                    if len(s) > len(buyw):
                        if len(s) > 1 and not isfloat(s):
                            buyw.append(s)
                if isfloat(olds) and s == 'C':
                    pocs.append('C')
                    strikes.append(olds)
                if isfloat(olds) and s == 'P':
                    pocs.append('P')
                    strikes.append(olds)
                if '/' in s:
                    expiries = (s)
                if 'next' in olds and 'week' in s:
                    expiries = 'next week' 
                if 'this' in olds and 'week' in s:
                    expiries = 'this week' 
                if 'at' in olds and isfloat(s):
                    prices.append(s)
                olds = s
                
                
            while len(prices) < len(buyw) or len(strikes) < len(buyw) or len(pocs) < len(buyw):
                if len(prices) < len(buyw):
                    prices.append('')

                if len(strikes) < len(buyw):
                    strikes.append('')
                if len(pocs) < len(buyw):
                    pocs.append('')
        sellw = []
        if len(sells) <= 1:
            sellw = []
        else:
            olds = ""
            for s in sells:
                if s in tickers:
                    if len(s) > len(sellw):
                        if len(s) > 1 and not isfloat(s):
                            sellw.append(s)
                if isfloat(olds) and s == 'C':
                    pocs.append('C')
                    strikes.append(olds)
                if isfloat(olds) and s == 'P':
                    pocs.append('P')
                    strikes.append(olds)
                if '/' in s:
                    expiries = (s)
                if 'next' in olds and 'week' in s:
                    expiries = 'next week' 
                if 'this' in olds and 'week' in s:
                    expiries = 'this week' 
                if 'at' in olds and isfloat(s):
                    prices.append(s)
                olds = s
            while len(prices) < len(sellw) or len(strikes) < len(sellw) or len(pocs) < len(sellw):
                if len(prices) < len(sellw):
                    prices.append('')

                if len(strikes) < len(sellw):
                    strikes.append('')
                if len(pocs) < len(sellw):
                    pocs.append('')
        if none is not None and len(nonew) > 0:
            with open("test.csv", "a") as myfile:
                print(buy)  
                
                for i in range(0, len(nonew)):
                    myfile.write(str(tweet.created_at)+',,' + pocs[i] + ',' + nonew[i]+',' + strikes[i] + ',' + prices[i] + ',' + expiries + '\n')

            #print('buy ticker: ' + buyw + ' and buy string: ' + buy)    
        if buy is not None and len(buyw) > 0:
            with open("test.csv", "a") as myfile:
                print(buy)  
                
                for i in range(0, len(buyw)):
                    myfile.write(str(tweet.created_at)+',buy,' + pocs[i] + ',' + buyw[i]+',' + strikes[i] + ',' + prices[i] + ',' + expiries + '\n')

            #print('buy ticker: ' + buyw + ' and buy string: ' + buy)
        elif sell is not None and len(sellw) > 0:
            with open("test.csv", "a") as myfile:
                for i in range(0, len(sellw)):
                    myfile.write(str(tweet.created_at)+',sell,' + pocs[i] + ',' + sellw[i]+',' + strikes[i] + ',' + prices[i] + ',' + expiries + '\n')
        #else:
            #print(s)
            #print('sell ticker: ' + sellw + ' and sell string: ' + sell)
        #print('buy: ' + buy)
        #print('sell: ' + sell)    

    public_tweets = api.user_timeline(screen_name = 'ducksquadpicks', max_id = max_id)
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

public_tweets = api.user_timeline(screen_name = 'ducksquadpicks')
dotweets(public_tweets)
