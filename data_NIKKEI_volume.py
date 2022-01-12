import pandas_datareader.data as web
import datetime
import csv

year = '22'
month = '01'

start = datetime.datetime(2022, 1, 1)
end = datetime.datetime(2022, 1, 31)
tsd = web.DataReader("^N225", "yahoo", start, end)
print(tsd)

with open(f'./20220110_NIKKEI/csv/{year}{month}Volume.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(tsd['Volume'])