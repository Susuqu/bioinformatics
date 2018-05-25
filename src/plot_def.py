# -*-coding:utf-8 -*-

# @PROJECT  : plot
# @Time     : 2018/05/25
# @Author   : Qu Susu
# @Mail     : qususu2012@126.com
# @File     : plot_def.py
# @Software : Pycharm

'''
Aim:
    1.汇总目前已经掌握的绘图技巧;
    2.之前写的脚本都是不断的调试的、而且是针对特定的数据，没有普适性，这里主要是汇总之前的一些经验，然后写成简单的函数，方便以后直接调用;

技巧：
    1.绘图基本我常用的就是DataFrame为基础的数据结构，通过pandas对DF提取某一列或者用groupby、count等操作都比较方便；
    2.绘图的难点是不知道要用什么数值呈现什么样的图，而不是代码的实现，所以在拿到数据的时候首先要思考要对哪些数值、呈现什么样的图，再着手处理；
    3.处理杂乱的文本数据时，在进行正式的绘图之前，要有数据清洗的意识：比如缺失值的填补、读取进来的数据类型等；
    4.文本各种读取转换的时候，encode的方式不对就会各种报错（'gb2312'，'utf-8'...来回试吧）；

种类：
    感觉特别好的一个关于绘图的文档：https://www.cnblogs.com/jasonfreak/p/5441512.html
    1.描述性统计分析(descriptiveStat)；
    2.绘图显示基本设置：坐标轴、title等字体、刻度、显示设置，开启网格，设置图片尺寸；
    3.散点图——
    4.折线图——
    5.柱形图——
    6.直方图——
    7.箱形图——
    8.在同一副图中绘制多个组别的数据
    9.在同一个画布上绘制多副子图

'''
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

from numpy import array,mean, median, ptp, var, std, cov, corrcoef
from scipy.stats import mode
from matplotlib.ticker import MultipleLocator, FormatStrFormatter   #matplotlib绘图设置坐标轴刻度大小和刻度


# 描述性统计分析：用NumPy和SciPy进行基本分析【待补充添加的协方差cov和相关系数corrcoef】
# data=table["adhdp"].dropna().sort_values().values #注意values后面没有括号
def descriptiveStat(data):
    # 中心位置（均值、中位数、众数）
    print(mean(data))
    print(median(data))
    print(mode(data))
    # 发散程度（极差、方差、标准差、变异系数）
    print(ptp(data))
    print(var(data))
    print(std(data))
    cv=mean(data)/std(data)    #变异系数
    print(cv)
    # 偏差程度（Z-分数）
    Zscore=(data[0] - mean(data)) / std(data)
    print(Zscore)

# 绘图显示基本设置，参见：plot_test_temp.py
# pic=plt画好的图
def plotFormat(pic):
    yFormatter=FormatStrFormatter('%.1f')   #y轴刻度显示保留1位小数
    ymajorLocator= MultipleLocator(0.2) #y轴主刻度间隔为0.2
    yminorLocator= MultipleLocator(0.1) #y轴副刻度间隔为0.1
    xmajorLocator= MultipleLocator(50)
    xminorLocator= MultipleLocator(25)
    plt.figure(1,figsize=(10,12))   #设置图片大小
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


# 探索分析（箱形图）
def drawBox(data,title):
    plt.boxplot([data],labels=["title"])
    plt.title('{}'.format(title))
    plt.savefig(r'E:\OuMengCompany\Project\plot_tmp\fig' + os.sep + '{}.{}'.format(title, '.png'))
    plt.show()

# 散点图：折线图和散点图绘制之前要先对值进行排序，否则乱序，看不出规律啊
# x=range(0,len(y_p))
# y=table["adhdp"].sort_values()

def drawScatter(x,y,title):
    plt.scatter(x,y,label=title,s=2,color='r')  #散点图
    # plt.scatter(x1,y1,label=title,s=2,color='b') #在同一副图中绘制多个组别的多条线
    plt.savefig(r'E:\OuMengCompany\Project\plot_tmp\fig' + os.sep + '{}.{}'.format(title, '.png'))
    plt.show()
