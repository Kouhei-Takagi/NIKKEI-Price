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
end_date=(f"{today.year}/{today.month}/{today.day}")
past=today - relativedelta(months=2)
past_date=(f"{past.year}/{past.month}/{past.day}")
yesterday=today - relativedelta(days=2)
yesterday_date=(f"{yesterday.year}/{yesterday.month}/{yesterday.day}")

# Get the data
start=past_date
end=end_date
n225=pdr.DataReader("NIKKEI225", "fred", start, end).dropna()

# Transform the data and fit it to the model
ln_n225=np.log(n225.dropna())
ln_n225.columns=['Close']
y=ln_n225
x=range(len(ln_n225))
x=sm.add_constant(x)
model=sm.OLS(y, x)
results=model.fit()

# Plot the data
plt.plot(y, label='Close', color="blue")
results.fittedvalues.plot(label='prediction', style='--')
plt.ylabel('log(n225 index)')
plt.legend(loc='upper left')
#plt.show()

# Calculate predictions and current data
n225_Today_data=pdr.DataReader("NIKKEI225", "fred", start, end).dropna()
n225_Today=np.log(n225_Today_data.dropna())
n225_Today_INT=int(np.exp(n225_Today.iloc[-1]))

future_Results=results.params[0]+results.params[1]*(len(x)+1)
future_Prediction=int(np.exp(future_Results))
#print(f'0日後の予想終値は、¥{future_Prediction}、現在値との差は、¥{future_Prediction-n225_Today}、乖離率は、{round(100*(future_Prediction-n225_Today)/n225_Today, 3)}%')

future_Results2=results.params[0]+results.params[1]*(len(x)+2)
future_Prediction2=int(np.exp(future_Results2))
#print(f'1日後の予想終値は、¥{future_Prediction2}、現在値との差は、¥{future_Prediction2-n225_Today}、乖離率は、{round(100*(future_Prediction2-n225_Today)/n225_Today, 3)}%')

future_Results3=results.params[0]+results.params[1]*(len(x)+3)
future_Prediction3=int(np.exp(future_Results3))
#print(f'2日後の予想終値は、¥{future_Prediction3}、現在値との差は、¥{future_Prediction3-n225_Today}、乖離率は、{round(100*(future_Prediction3-n225_Today)/n225_Today, 3)}%')

# Create Twitter message
tweet_word=f'現在の日経平均株価は、￥{n225_Today_INT}です。1日後の日経平均株価の予想終値は、¥{future_Prediction}です。乖離率は、{round(100*(future_Prediction-n225_Today_INT)/n225_Today_INT, 3)}%です。\nhttps://www.creatingfavoriteopinions.com \n#日経平均株価 #NIKKEI225'

# Print tweet message
print(tweet_word)

# Tweet tweet message
#api.update_status(tweet_word)