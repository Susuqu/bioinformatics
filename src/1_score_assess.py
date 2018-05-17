# -*-coding:utf-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from pylab import *
import seaborn as sns
import scipy
from scipy import stats


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
print(len(control)) # 92
print(len(case))    #189

# t检验
# 两独立样本t检验：先用stats.levene判断方差齐性，然后如果非齐性则要在加入stats.ttest_ind(默认方差是齐性的)中加入参数——equal_var = False
def ttest(colname):
    p_levene=stats.levene(case[colname].dropna().values,control[colname].dropna().values).pvalue
    print(p_levene)
    '''
    print(stats.levene(case[u'倒背'].dropna().values,control[u'倒背'].dropna().values))
    LeveneResult(statistic=0.8593739556288843, pvalue=0.35471516924984425)，p值远大于0.05，认为两总体具有方差齐性。
    '''
    if p_levene<0.05:
        print('{}{}{}'.format(colname,":",stats.ttest_ind(case[colname].dropna().values, control[colname].dropna().values, equal_var=False).pvalue))
    else:
        print('{}{}{}'.format(colname,"在case和control之间的P-value:",stats.ttest_ind(case[colname].dropna().values, control[colname].dropna().values).pvalue))

namelist=[u'正背',u'倒背',u'数字广度粗分',u'数字广度量表分']
for name in namelist:
    ttest(colname=name)
'''
正背在case和control之间的P-value:0.8041959437085187
倒背在case和control之间的P-value:0.20787065720005246
数字广度粗分在case和control之间的P-value:0.6841430097226837
数字广度量表分在case和control之间的P-value:0.051395256884453074
'''

sys.exit()
# 计算直方图的bins数目

'''
https://blog.csdn.net/denny2015/article/details/50581784

'''

'''
some useful website:
总结的方式值得借鉴：简单明了    https://blog.csdn.net/elecjack/article/details/50776199
pandas聚合：https://www.cnblogs.com/huiyang865/p/5577772.html
pandas stack：https://blog.csdn.net/SecondLieutenant/article/details/79499930
matplotlib详解图像的各个部分：很好的笔记   https://www.cnblogs.com/nju2014/p/5620776.html
描述性统计分析：很好的笔记   https://www.cnblogs.com/jasonfreak/p/5441512.html
pandas数据清洗的思想：  https://blog.csdn.net/zhili8866/article/details/68134481

'''

# 在同一个图里分别画case和control的频数分布直方图，看两个分布的重叠情况；
# 在同一个图里分别画case和control的频数分布直方图，同时通过seaborn绘制拟合曲线；
def drawCaseControlHist(case,control,colname,filename):
    case_data=case[colname].dropna().sort_values().values
    # print(case_data)
    control_data=control[colname].dropna().sort_values().values
    # print(col_value)
    plt.hist(case_data,bins=30,label='case',color='red',histtype= 'step')
    plt.hist(control_data,bins=30,label='control', color='blue',histtype= 'step')
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('{}{}'.format(colname,' 在ADHD患者（Case）和健康对照（Control）中的分布情况'))
    plt.legend(loc='best')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\score'+os.sep+'{}_{}.{}'.format(filename,colname,'png'))
    plt.show()
    plt.close()
    # 注意上面的图画完了要有plt.close(),否则和下面的图会同时出现在一个画布里。
    # 通过seaborn绘制拟合曲线
    sns.set_palette("hls")  #设置所有图的颜色，使用hls色彩空间
    sns.distplot(case_data, bins=15, kde=True, color='r',label='case')   #kde=True表示是否显示拟合曲线
    sns.distplot(control_data,bins=15,kde=True,color='b',label='control')
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('{}{}'.format(colname,' 在ADHD患者（Case）和健康对照（Control）中的分布情况'))
    plt.legend(loc='best')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\score' + os.sep + '{}_{}_{}.{}'.format(filename, colname,'line','png'))
    plt.show()
    plt.close()

# namelist=[u'数字广度粗分']
namelist=[u'正背',u'倒背',u'数字广度粗分',u'数字广度量表分']
for name in namelist:
    drawCaseControlHist(colname=name,case=case,control=control,filename='CompareCaseConHist')

# sys.exit()
# 分别单独绘制case和control的hist图，看下分布情况；
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

