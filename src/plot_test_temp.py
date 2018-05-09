# -*-coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

'''
发现绘图难点是不知道要用什么数值呈现什么样的图，而不是代码的实现！！
对adhdp 和adhdt分别绘制折线图，尝试过后发现折线图效果并不好，所以改成画散点图。
折线图和散点图绘制之前要先对值进行排序，否则乱序。

'''

table = pd.read_table("tmp.txt", encoding='gb2312')
# adhdp
y_p=table["adhdp"].sort_values()
x_p=range(0,len(y_p))
print(x_p)
# adhdt
y_t=table["adhdt"].sort_values()
x_t=range(0,len(y_t))
print(x_t)

plt.scatter(x_p,y_p,label='adhdp in all sample',s=1,color='r')
plt.scatter(x_t,y_t,label='adhdt in all sample',s=1,color='b')
# 折线图
# plt.plot(x,adhdp,label='adhdp in all sample',linewidth=1,color='r',marker='o',markerfacecolor='blue',markersize=12)
# plt.plot(x,adhdt,label='adhdt in all sample')
plt.xlabel('Plot Number of sample')
plt.ylabel('ratio')
plt.title('Distribution of adhdp and adhdt ratio in all sample')
plt.legend()
plt.show()