# -*-coding:utf-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter   #matplotlib绘图设置坐标轴刻度大小和刻度

'''
这个文档主要是对绘图时细节优化进行测试的脚本，优化方面包括：
    title：字体，大小；
    坐标轴：刻度，字体，大小；

summary:
1.发现绘图难点是不知道要用什么数值呈现什么样的图，而不是代码的实现；
2.处理这种杂乱的文本数据时，有个操作很关键——数据清洗，比如缺失值的填补、读取进来的数据类型等；
    na_values : list-like, default None
    List of additional strings to recognize as NA/NaN
3.其他细节：
    折线图和散点图绘制之前要先对值进行排序，否则乱序，看不出规律啊；
    根据“索引”或者“值”对series和dataframe进行排序不一样啊；
    
'''
table = pd.read_table("tmp.txt", encoding='gb2312',na_values=[" ","-","NONE",'X'])  #清洗数据
table[['adhdp','adhdt']]=table[['adhdp','adhdt']].astype(float) # 转换数据类型
y_p=table["adhdp"].sort_values()
# print(y_p)
x_p=range(0,len(y_p))
# print(x_p)
y_t=table["adhdt"].sort_values()
x_t=range(0,len(y_t))
# print(x_t)

yFormatter=FormatStrFormatter('%.1f')   #y轴刻度显示保留1位小数
ymajorLocator= MultipleLocator(0.2) #y轴主刻度间隔为0.2
yminorLocator= MultipleLocator(0.1) #y轴副刻度间隔为0.1
xmajorLocator= MultipleLocator(50)
xminorLocator= MultipleLocator(25)
plt.figure(1,figsize=(10,12))   #设置图片大小
plt.scatter(x_p,y_p,label='adhdp in all sample',s=2,color='r')  #散点图
plt.scatter(x_t,y_t,label='adhdt in all sample',s=2,color='b')

ax=plt.gca() # 获取当前的坐标轴，gca=get current axis，之后对坐标轴字体等操作都是在ax基础上进行的，因为一般不直接对plt设置属性
ax.yaxis.set_major_formatter(yFormatter)
ax.yaxis.set_major_locator(ymajorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_minor_locator(xminorLocator)
# ax.yaxis.grid(True, which='minor') #只开启Y轴对应的网格
ax.grid()   #开启全部的网格

for ind, label in enumerate(ax.yaxis.get_ticklabels()):
    if ind % 2 == 0:  # every 10th label is kept
        label.set_visible(True)
    else:
        label.set_visible(False)

# 设置刻度文本的大小和刻度值的字体大小
plt.tick_params(labelsize=16)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

# 设置坐标轴显示的文字/字体大小/字体
ax.set_xlabel('Plot Number of sample',fontsize=18,fontname='Times New Roman')  #不要直接用plt.xlabel('Plot Number of sample')，没法设置字体大小
ax.set_ylabel('Ratio of sample',fontsize=18,fontname='Times New Roman')
ax.set_title('Distribution of adhdp and adhdt ratio in all sample',fontsize=23,fontname='Times New Roman')
ax.legend(fontsize=15)
plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig'+os.sep+'test_distribution_ratio.png')
plt.show()
