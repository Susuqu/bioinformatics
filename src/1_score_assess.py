# -*-coding:utf-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

data = pd.read_table("1_score_arrange.txt", encoding='gbk',na_values=[" ","-","NONE",'X','#VALUE!','#DIV/0!'])
# print(data.shape)   #(282, 10)

mpl.rcParams['font.sans-serif'] = ['SimHei']    #这一行必须加，否则u的作用就无法实现

# 分别对以下列（分类变量）绘制bar plot: 月龄，性别，诊断
def drawBar(colname):
    data[colname].value_counts().plot(kind='bar')
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Number of sample')
    plt.title('distribution in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\score'+os.sep+'{}.{}'.format(colname,'png'))
    plt.show()
    plt.close()
# drawBar(colname=u'月龄')  #可见月龄绘制的bar图效果并不够好
# drawBar(colname=u'性别')
# drawBar(colname=u'诊断')

# 分别对以下列（分类变量）绘制bar plot: 月龄，正背，倒背，数字广度粗分，数字广度量表分
def drawHist(colname,groupnumber):
    col_value=data[colname].dropna().sort_values().values
    # print(col_value)
    plt.hist(col_value,groupnumber)
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\score'+os.sep+'{}.{}'.format(colname,'png'))
    plt.show()
    plt.close()

# namelist=[u'月龄',u'正背',u'倒背',u'数字广度粗分',u'数字广度量表分']
# for name in namelist:
#     drawHist(colname=name,groupnumber=40)

# sub group by 诊断，性别，月龄
def drawSubBar(colname,subname,kind):
    data[[subname, colname]].groupby([colname, subname]).数字广度粗分.count().unstack().plot(kind=kind,stacked=True)  # 默认的为line
    # print(col_value)
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\score'+os.sep+'{}_{}_{}.{}'.format(colname,subname,kind,'png'))
    plt.show()
    plt.close()

# drawSubBar(colname=u'数字广度粗分',subname=u'诊断',kind='line')
# drawSubBar(colname=u'数字广度粗分',subname=u'性别',kind='line')
# drawSubBar(colname=u'数字广度粗分',subname=u'月龄',kind='line')
# drawSubBar(colname=u'数字广度量表分',subname=u'诊断',kind='line')
# drawSubBar(colname=u'数字广度量表分',subname=u'性别',kind='line')
# drawSubBar(colname=u'数字广度量表分',subname=u'月龄',kind='line')
# drawSubBar(colname=u'正背',subname=u'诊断',kind='line')
# drawSubBar(colname=u'正背',subname=u'性别',kind='line')
# drawSubBar(colname=u'正背',subname=u'月龄',kind='line')
# drawSubBar(colname=u'倒背',subname=u'诊断',kind='line')
# drawSubBar(colname=u'倒背',subname=u'性别',kind='line')
# drawSubBar(colname=u'倒背',subname=u'月龄',kind='line')

# 其实我还想做个卡方检验，可是来不及了