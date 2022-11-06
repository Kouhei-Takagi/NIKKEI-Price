import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import pandas as pd

start="2020/1/1"
end="2022/10/31"

price=pdr.DataReader("^N225", 'yahoo', start, end)

fx=pdr.DataReader('DEXJPUS',"fred",start,end)
port=pd.concat([price.Close,fx],axis=1).dropna()
n=port.Close.pct_change().dropna()
f=port.DEXJPUS.pct_change().dropna()
f.rolling(window=20).corr(n).plot(color="blue")
plt.ylabel("correlation")

plt.show()