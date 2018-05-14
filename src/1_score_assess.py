# -*-coding:utf-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *

'''
缺失值的替换不成功；
ADHD诊断分组时，为什么有两个ADHD-C好像？是不是数据清洗还是什么过程有问题？——找到了问题出在哪里：原来是有一个ADHD-C后面多了一个空格，所以被当成了两个类别。

'''
data = pd.read_table("1_score_arrange.txt", encoding='utf-8',na_values=[" ","-","NONE",'X','#VALUE!'])
# print(data.shape)   #(282, 10)
# df.loc[df['columnName']=='the value']

mpl.rcParams['font.sans-serif'] = ['SimHei']    #这一行必须加，否则u的作用就无法实现

control=data.loc[data[u'诊断']=='NC']
case=data.loc[data[u'诊断']!='NC']
# print(case)

def drawCaseHist(df,colname,groupnumber,filename):
    col_value=df[colname].dropna().sort_values().values
    # print(col_value)
    plt.hist(col_value,groupnumber)
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\score'+os.sep+'{}_{}.{}'.format(filename,colname,'png'))
    plt.show()
    plt.close()

namelist=[u'数字广度粗分',u'数字广度量表分']
# namelist=[u'月龄',u'正背',u'倒背',u'数字广度粗分',u'数字广度量表分']
for name in namelist:
    drawCaseHist(colname=name,groupnumber=15,df=case,filename='case')
    drawCaseHist(colname=name, groupnumber=15, df=control,filename='control')


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