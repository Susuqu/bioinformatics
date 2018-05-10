# -*-coding:utf-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt


'''
我记得有个公式可以评估分多少组是合适的来着？
'''
table = pd.read_table("tmp.txt", encoding='gb2312',na_values=[" ","-","NONE",'X'])  #清洗数据
table[['adhdp','adhdt']]=table[['adhdp','adhdt']].astype(float)# 转换数据类型

# table['adhdp'].replace({np.nan:-99})  #为啥就是替换不成功呢

y_p=table["adhdp"].dropna().sort_values().values #注意values后面没有括号
y_t=table["adhdt"].dropna().sort_values().values
# print(y_p)

# 绘制直方图的时候必须得去除nan的点，否则报错；我本想用-99替换缺失值这样来看下大概多大比例的位点缺失，但是一直替换不成功
def drawHist(ratiovalue,title,groupnumber):
    plt.hist(ratiovalue,groupnumber)
    plt.xlabel('ratio')
    plt.ylabel('Frequency')
    plt.title('distribution of ratio in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig'+os.sep+'{}.{}'.format(title,'.png'))
    plt.show()

drawHist(ratiovalue=y_p,title='test_adhdp_distribution ',groupnumber=100)
drawHist(ratiovalue=y_t,title='test_adhdt_distribution ',groupnumber=100)

# 探索分析（箱形图）
def drawBox(ratiovalue,title):
    plt.boxplot([ratiovalue],labels=["title"])
    plt.title('{}'.format(title))
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig' + os.sep + '{}.{}'.format(title, '.png'))
    plt.show()

drawBox(ratiovalue=y_p,title='test_adhdp_boxplot ')
drawBox(ratiovalue=y_t,title='test_adhdt_boxplot ')

###使用NumPy和SciPy进行基本分析
from numpy import array,mean, median, ptp, var, std, cov, corrcoef
from scipy.stats import mode    #pip install scipy
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

    # 计算两组数据的相关程度：协方差cov和相关系数corrcoef衡量
    # corrcoef(array([data1,data2]))

descriptiveStat(data=y_p)
descriptiveStat(data=y_t)
# codata=array([y_p,y_t])
# print(cov(codata,bias=1))
# print(corrcoef(array([y_p,y_t])))