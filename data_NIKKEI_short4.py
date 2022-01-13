import os
import csv

year = '21'
month = '10'
pathOrigin = './20220110_NIKKEI/text/'
new_list = []
final_list = []

def short_ratio(nameNum):
    new_path = f'{pathOrigin}{year}{month}{nameNum}-m.txt'
    with open(new_path) as f:
        contents = f.readlines()[44]
        new_list.append(contents)
        #print(new_list)

for i in range(32):
    if i < 10:
        num = f'0{i}'
        path_Under = f'{pathOrigin}{year}{month}{num}-m.txt'
        if(os.path.exists(path_Under)):
            short_ratio(num)
    else:
        num = i
        path_Over = f'{pathOrigin}{year}{month}{num}-m.txt'
        if(os.path.exists(path_Over)):
            short_ratio(i)

#print(new_list)
for list in new_list:
    list = list.replace('%\n', '')
    final_list.append(list)

print(final_list)

path_final = f'./20220110_NIKKEI/csv/{year}{month}short.csv'
with open(path_final, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(final_list)