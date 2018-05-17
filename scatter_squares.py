import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
# s 为点的大小
#plt.scatter(x_values,y_values,c='red',s=10)
# plt.cm 决定使用哪个颜色映射
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',
    s=40)
plt.scatter(500,240000,edgecolor='none',s=40) 

plt.title('Square Numbers',fontsize=24)
plt.xlabel('Value',fontsize=14)
plt.ylabel('Square Value',fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both',which='major',labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])

plt.show()
