import pandas_datareader.data as pdr
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

start="1945/5/16"
end="2022/10/31"
n225=pdr.DataReader("NIKKEI225", 'fred',start,end)

struct_break=[('1945/5/16', 'recv'),('1954/12/1','growth'),('1972/1/1','stable'),('1986/12/1','bubble'),('1991/3/1','reform')]

fig=plt.figure()
g=fig.add_subplot(1,1,1)
ln_n225=np.log(n225)
ln_n225.plot(ax=g,style='y-',linewidth=0.5)

for date, label in struct_break:
    g.annotate(label,xy=(date,ln_n225.asof(date)),
        xytext=(date,ln_n225.asof(date)-0.75),
        horizontalalignment='left',verticalalignment='top')
    g.set_xlim([start,end])

plt.ylabel('log(N225 index)')
plt.title('Log Nikkei 225 index and structual change')

plt.show()
print('done')