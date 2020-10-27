import json
import pygal
import math

filename='matplotlib_test/chapter16/btc_close_2017.json'
with open(filename) as f:
    btc_data=json.load(f)

dates=[]
months=[]
weeks=[]
weekdays=[]
closes=[]
for bct_dict in btc_data:
    dates.append(bct_dict['date'])
    months.append(int(bct_dict['month']))
    weeks.append(int(bct_dict['week']))
    weekdays.append(bct_dict['weekday'])
    closes.append(int(float(bct_dict['close'])))

line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='收盘价（￥）'
line_chart.x_labels=dates
N=20
line_chart.x_labels_major=dates[::N]
close_log=[math.log10(_) for _ in closes]
line_chart.add('收盘价',close_log)
line_chart.render_to_file('收盘价折线图log.svg')