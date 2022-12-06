import pandas_datareader.data as pdr
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import tweepy
import configparser

# Configure ConfigParser
conf=configparser.ConfigParser()
conf.read('./Tweetbot/config.ini')

# Retrieve Twitter credentials
API_KEY=conf['Tweetbot']['API_KEY']
API_SECRET=conf['Tweetbot']['API_SECRET']
ACCESS_TOKEN=conf['Tweetbot']['ACCESS_TOKEN']
ACCESS_SECRET=conf['Tweetbot']['ACCESS_SECRET']

# Setup the connection to Twitter API 
auth=tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api=tweepy.API(auth)

# Get the dates for the data
today=datetime.today()
end_date=f"{today.year}/{today.month}/{today.day}"
past=today - relativedelta(days=20)
past_date=f"{past.year}/{past.month}/{past.day}"
yesterday=today - relativedelta(days=2)
yesterday_date=f"{yesterday.year}/{yesterday.month}/{yesterday.day}"

# Get the data
start=past_date
end=end_date
ETH=pdr.DataReader("ETH-JPY", "yahoo", start, end).dropna()

# Transform the data and fit it to the model
ln_ETH=np.log(ETH.iloc[:,3].dropna())
ln_ETH.columns=['Close']
y=ln_ETH
x=range(len(ln_ETH))
x=sm.add_constant(x)
model=sm.OLS(y, x)
results=model.fit()

# Plot the data
plt.plot(y, label='Close', color="blue")
results.fittedvalues.plot(label='prediction', style='--')
plt.ylabel('log(ETH index)')
plt.legend(loc='upper left')
#plt.show()

# Calculate predictions and current data
ETH_Today_Data=pdr.DataReader("ETH-JPY", "yahoo", start, end).dropna()
ETH_Today=np.log(ETH_Today_Data.iloc[:,3].dropna())
ETH_Today_INT=int(np.exp(ETH_Today[-1]))

future_Results=results.params[0]+results.params[1]*(len(x)+1)
future_Prediction=int(np.exp(future_Results))
#print(f'0日後の予想終値は、¥{future_Prediction}、現在値との差は、¥{future_Prediction-ETH_Today}、乖離率は、{round(100*(future_Prediction-ETH_Today)/ETH_Today, 3)}%')

future_Results2=results.params[0]+results.params[1]*(len(x)+2)
future_Prediction2=int(np.exp(future_Results2))
#print(f'1日後の予想終値は、¥{future_Prediction2}、現在値との差は、¥{future_Prediction2-ETH_Today}、乖離率は、{round(100*(future_Prediction2-ETH_Today)/ETH_Today, 3)}%')

future_Results3=results.params[0]+results.params[1]*(len(x)+3)
future_Prediction3=int(np.exp(future_Results3))
#print(f'2日後の予想終値は、¥{future_Prediction3}、現在値との差は、¥{future_Prediction3-ETH_Today}、乖離率は、{round(100*(future_Prediction3-ETH_Today)/ETH_Today, 3)}%')

# Create Twitter message
tweet_word=f'現在のETH-JPYは、￥{ETH_Today_INT}です。1日後のETH-JPYの予想終値は、¥{future_Prediction}です。乖離率は、{round(100*(future_Prediction-ETH_Today_INT)/ETH_Today_INT, 3)}%です。\nhttps://www.creatingfavoriteopinions.com \n#ETH #ethereum'

# Print tweet message
print(tweet_word)

# Tweet tweet message
#api.update_status(tweet_word)