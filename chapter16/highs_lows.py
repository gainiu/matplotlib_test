import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename='matplotlib_test/chapter16/death_valley_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    for index,column_header in enumerate(header_row):
        print(index,column_header)
    
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date=datetime.strptime(row[0],'%Y-%m-%d')
            high=int(row[1])
            low=int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
fig=plt.figure(figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

plt.title('Daily high temperature, July 2014',fontsize=24)
plt.xlabel('',fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize=14)
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()