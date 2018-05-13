# -*-coding:utf-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

'''
plot可以优化的点：subgroup画图的循环怎么实现？
缺失值的替换不成功；
'''
data = pd.read_table("2_drug_arrange.txt", encoding='utf-8',na_values=[" ","-","NONE",'X','#VALUE!','#DIV/0!'])    #为啥文件名是中文的时候就有问题呢？
# print(data.shape)   #(468,31)
# print(data['ssattp1'])  #看下空值之类的是否替换成功

# 分别对以下列（分类变量）绘制bar plot: pharm, sex, subtype
def drawBar(colname):
    data[colname].value_counts().plot(kind='bar')
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Number of sample')
    plt.title('distribution in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug'+os.sep+'{}.{}'.format(colname,'png'))
    plt.show()
    plt.close()
# drawBar(colname='pharm')
# drawBar(colname='sex')
# drawBar(colname='subtype')

# 分别对以下列（分类变量）绘制hist plot: iq, age, adhdpr1, adhdpr, atScoreP, atRatioP, hiScoreP, hiRatioP, adhdtr1, adhdtr, atScoreT, atRatioT, hiScoreT, hiRatioT
def drawHist(colname,groupnumber):
    col_value=data[colname].dropna().sort_values().values
    # print(col_value)
    plt.hist(col_value,groupnumber)
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug'+os.sep+'{}.{}'.format(colname,'png'))
    plt.show()
    plt.close()

# 应该写循环的啊，哭
# drawHist(colname='age',groupnumber=20)
# drawHist(colname='iq',groupnumber=90)
# drawHist(colname='adhdpr1',groupnumber=70)    #父母评分用药前后减分——量表总分
# drawHist(colname='adhdpr',groupnumber=200)    #父母评分用药前后减分比率——量表总分
# drawHist(colname='atScoreP',groupnumber=100)   #父母评分用药前后减分——注意缺陷分量表分数
# drawHist(colname='atRatioP',groupnumber=100)   #父母评分用药前后减分比率——注意缺陷分量表分数
# drawHist(colname='hiScoreP',groupnumber=70)   #父母评分用药前后减分——多动冲动分量表分数
# drawHist(colname='hiRatioP',groupnumber=200)  #父母评分用药前后减分比率——多动冲动分量表分数
# drawHist(colname='adhdtr1',groupnumber=90)    #教师评分用药前后减分——量表总分
# drawHist(colname='adhdtr',groupnumber=120)    #教师评分用药前后减分比率——量表总分
# drawHist(colname='atScoreT',groupnumber=50)   #教师评分用药前后减分——注意缺陷分量表分数
# drawHist(colname='atRatioT',groupnumber=130)   #教师评分用药前后减分比率——注意缺陷分量表分数
# drawHist(colname='hiScoreT',groupnumber=50)   #教师评分用药前后减分——多动冲动分量表分数
# drawHist(colname='hiRatioT',groupnumber=150)  #教师评分用药前后减分比率——多动冲动分量表分数

# adhdpr1, adhdpr, atScoreP, atRatioP, hiScoreP, hiRatioP, adhdtr1, adhdtr, atScoreT, atRatioT, hiScoreT, hiRatioT
# groupby sex, subtype, pharm


def drawSubBar(colname,subname,kind,a,b,c,d):
    # data[[subname, colname]].groupby([colname, subname]).hiRatioP.count().unstack().plot(kind=kind,stacked=True)  # 默认的为line
    plt.subplot2grid((a,b),(c,d),colspan=3)
    print(a,b,c,d)
    '''
    表示将整个图像窗口分成a行b列
    a=1
    b=3
    c,d表示小图在大图中的位置
    '''
    data.groupby([colname, subname])[[colname]].count().unstack().plot(kind=kind, stacked=True)
    # print(col_value)
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.legend(loc='best')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drugNew'+os.sep+'{}_{}_{}.{}'.format(colname,subname,kind,'png'))
    # plt.show()
    # plt.close()

# colnamelist=['adhdpr1', 'adhdpr', 'atScoreP', 'atRatioP', 'hiScoreP', 'hiRatioP', 'adhdtr1', 'adhdtr', 'atScoreT', 'atRatioT', 'hiScoreT', 'hiRatioT']
# subnamelist=['sex','pharm','subtype']
# plotkind=['bar','line']
# for name in colnamelist:
#     for sub in subnamelist:
#         for style in plotkind:
#             drawSubBar(colname=name,subname=sub,kind=style)
# colnamelist=['adhdpr1', 'adhdpr', 'atScoreP', 'atRatioP', 'hiScoreP', 'hiRatioP', 'adhdtr1', 'adhdtr', 'atScoreT', 'atRatioT', 'hiScoreT', 'hiRatioT']
plt.figure()
colnamelist=['adhdpr1']
subnamelist=['sex','pharm','subtype']
row=0
col=0
for name in colnamelist:
    for sub in subnamelist:
        drawSubBar(colname=name,subname=sub,kind='bar',a=1,b=3,c=row,d=col)
        col=col+1
    plt.show()
# plt.close()

# drawSubBar(colname='adhdpr1',subname='sex',kind='bar')
# drawSubBar(colname='adhdpr1',subname='sex',kind='line')
# drawSubBar(colname='adhdpr',subname='sex',kind='bar')
# drawSubBar(colname='adhdpr',subname='pharm',kind='line')
# drawSubBar(colname='adhdtr1',subname='sex',kind='bar')
# drawSubBar(colname='adhdtr1',subname='sex',kind='line')
# drawSubBar(colname='adhdtr',subname='sex',kind='bar')
# drawSubBar(colname='adhdtr',subname='subtype',kind='line')
# drawSubBar(colname='atRatioP',subname='pharm',kind='line')
# drawSubBar(colname='atRatioT',subname='subtype',kind='line')
# drawSubBar(colname='hiRatioP',subname='subtype',kind='line')
# drawSubBar(colname='hiRatioT',subname='pharm',kind='line')

# groupby sex, subtype, pharm
def testdrawSubBar(colname,subname,kind):
    # data[[subname, colname]].groupby([colname, subname]).count().unstack().plot(kind=kind,stacked=True)  # 默认的为line
    group_subname=data.groupby([colname, subname])[[colname]].count().unstack()
    print(group_subname)
    # data.groupby([colname,subname])[[colname,subname]].count().unstack().plot(kind=kind,stacked=True)#各自分布的叠加
    data.groupby([colname,subname])[[colname]].count().unstack().plot(kind=kind,stacked=True)  # colname分布为基础，subname中不同类别的分布是否一致
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.legend(('female','male'),loc='best')    #legend顺序是根据实际注明的
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug\test'+os.sep+'{}_{}_{}.{}'.format(colname,subname,kind,'png'))
    plt.show()
    plt.close()

# testdrawSubBar(colname='adhdpr1',subname='sex',kind='bar')
# drawSubBar(colname='adhdpr1',subname='sex',kind='line')