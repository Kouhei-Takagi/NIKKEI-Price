import pandas_datareader.data as pdr
import matplotlib.pyplot as plt

start="2020/1/1"
end="2022/10/31"
N225=pdr.DataReader("NIKKEI225", 'fred',start,end)

N225.plot(color='darkblue')
plt.ylabel('N225 index')

plt.show()