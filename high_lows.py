from matplotlib import pyplot as plt
import csv
from datetime import datetime

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 得到文件第一行
    #print(header_row)
    # enumerate 获取每个元素的索引及其值
    #for index,column_header in enumerate(header_row):
    #   print(index,column_header)
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],'%Y-%m-%d')
            low = int(row[3])
        except ValueError:
            print(current_date,'missing data')
        else:
            highs.append(int(row[1]))
            dates.append(current_date)
            lows.append(low)
            
    #print(highs)
    fig = plt.figure(dpi=128,figsize=(10,6))
    # 折线图,scatter:点状图
    # alpha 设置透明度
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.3)
                     
    plt.title('Daily high and low temperatures, 2014',fontsize=24)
    plt.xlabel('',fontsize=16)
    
    # 绘制斜的日期标签，以免重叠
    fig.autofmt_xdate()
    
    plt.ylabel('Temperature(F)',fontsize=16)
    #plt.tick_params(axis='both',which='major',labelsize=16)
    
    plt.show()
    
