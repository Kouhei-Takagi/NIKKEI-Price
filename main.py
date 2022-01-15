#from matplotlib import markers
from sys import builtin_module_names
from turtle import color
from numpy import float64
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('./20220110_NIKKEI/csv/2201Close_price.csv',header=None,sep=',', dtype=float64)
df2 = pd.read_csv('./20220110_NIKKEI/csv/2201Volume.csv',header=None,sep=',', dtype=float64)
df3 = pd.read_csv('./20220110_NIKKEI/csv/2201short.csv',header=None,sep=',', dtype=float64)

c = df1.loc[0,0:20].div(1000)
c.plot(color="blue", label="Close price")
v = df2.loc[0, 0:20].div(10000000)
v.plot(color="green", label="Volume")
s = df3.loc[0, 0:20]
s.plot(color="black", label="Selleing Volume")

plt.title('Close price, Volume and Selling Volume')
plt.legend()
plt.show()