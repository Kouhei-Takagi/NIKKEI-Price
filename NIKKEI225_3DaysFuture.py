import pandas_datareader.data as pdr
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

today=datetime.today()
end_date=(f"{today.year}/{today.month}/{today.day}")
past=today - relativedelta(weeks=4)
past_date=(f"{past.year}/{past.month}/{past.day}")

start=past_date
end=end_date

n225=pdr.DataReader("NIKKEI225", "fred", start, end).dropna()
ln_n225=np.log(n225.dropna())
ln_n225.columns=['Close']
y=ln_n225
x=range(len(ln_n225))
x=sm.add_constant(x)
model=sm.OLS(y, x)
results=model.fit()

plt.plot(y, label='Close', color="blue")
results.fittedvalues.plot(label='prediction', style='--')
plt.ylabel('log(n225 index)')
plt.legend(loc='upper left')

plt.show()

future_Results=results.params[0]+results.params[1]*(len(x)+1)
print(f'1日後の日経平均の予想終値は、¥{int(np.exp(future_Results))}です。')

future_Results2=results.params[0]+results.params[1]*(len(x)+2)
print(f'2日後の日経平均の予想終値は、¥{int(np.exp(future_Results2))}です。')

future_Results3=results.params[0]+results.params[1]*(len(x)+3)
print(f'3日後の日経平均の予想終値は、¥{int(np.exp(future_Results3))}です。')