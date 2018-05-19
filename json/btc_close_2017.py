'''
from urllib.request import urlopen
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
    
response = urlopen(json_url)

req = response.read()

with open('btc_close_2017_urllib.json','wb') as f:
    f.write(req)

file_urllib = json.loads(req)
print(file_urllib)
'''
import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)

with open('btc_close_2017_request.json','w') as f:
    f.write(req.text)
#file_requests = req.json()
#print(file_requests)

import json
filename = 'btc_close_2017.json'
with open(filename) as f:
    btc_data = json.load(f)



dates = []
months = []
weeks = []
weekdays = []
close = []
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))
    
import pygal

line_chart = pygal.Line(x_label_rotation=20,show_minor_x_label=False)
line_chart.title = '收盘价（人民币）'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
line_chart.add('收盘价',close)
line_chart.render_to_file('收盘价折线图.svg')
