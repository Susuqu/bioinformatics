# -*-coding:utf-8 -*-
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

'''
缺失值的替换不成功；
把图片都放在一张图上的时候label显示有点不好看；
其他已测试，无bug；
'''
data = pd.read_table("2_drug_arrange.txt", encoding='utf-8',na_values=[" ","-","NONE",'X','#VALUE!','#DIV/0!'])    #为啥文件名是中文的时候就有问题呢？
# print(data.shape)   #(468,31)
# print(data['ssattp1'])  #看下空值之类的是否替换成功

# 这两个list后面的函数或者方法都会用到的
# colnamelist=['adhdpr1', 'adhdpr', 'atScoreP', 'atRatioP', 'hiScoreP', 'hiRatioP', 'adhdtr1', 'adhdtr', 'atScoreT', 'atRatioT', 'hiScoreT', 'hiRatioT']
subnamelist=['sex','pharm','subtype']

#遗留的问题：减分率那种的话连续数值太多，所以画出来的图效果不好！

# plot sub plot in one picture
def drawSubHistOne(colname,subname,ax):
    case_data= data.groupby([colname, subname])[[colname]].count().unstack()
    col_value = data[colname].dropna().sort_values().values
    plt.hist(case_data, bins=50, label='case', histtype='step',stacked=True)
    # data.groupby([colname, subname])[[colname]].count().unstack().plot(kind='bar',stacked=True,ax=ax)
    ax.set_xlabel('{}'.format(colname))
    ax.set_ylabel('Frequency')
    ax.set_title('{}''{}'.format(subname,' distribution in all samples'))
    ax.legend(loc='best')#在合适的位置放置图例

colnamelist=['adhdpr']# for test
for name in colnamelist:
    fig2=plt.figure(figsize=(30,10))
    n = 1
    for sub in subnamelist:
        ax = fig2.add_subplot(1, 3, n)
        print()
        drawSubHistOne(colname=name,subname=sub,ax=ax)
        n=n+1
        ax = plt.gca()  # 获取当前的坐标轴，gca=get current axis，之后对坐标轴字体等操作都是在ax基础上进行的，因为一般不直接对plt设置属性
        # ax.xaxis.set_major_locator(xmajorLocator)
        # ax.xaxis.set_minor_locator(xminorLocator)
        for ind, label in enumerate(ax.yaxis.get_ticklabels()):
            if ind % 2 == 0:  # every 10th label is kept
                label.set_visible(True)
            else:
                label.set_visible(False)

    # plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug_new' + os.sep + '{}_{}.{}'.format(name,'sex_pharm_subtype','png'))
    plt.show()
    plt.close()

sys.exit()
############################################################################################
# 分别对以下列（分类变量）单独绘制bar plot: pharm, sex, subtype
def drawBarOne(colname,ax):
    data[colname].value_counts().plot(kind='bar',ax=ax)
    ax.set_xlabel('{}'.format(colname))
    ax.set_ylabel('Number of sample')
    ax.set_title('distribution in all samples')
    # plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug'+os.sep+'{}.{}'.format(colname,'png'))
    # plt.show()
    # plt.close()
#
# fig1=plt.figure(figsize=(30,10))
# n = 1
# for name in subnamelist:
#     ax = fig1.add_subplot(1, 3, n)
#     drawBarOne(colname=name,ax=ax)
#     n=n+1
# plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug_new'+os.sep+'{}.{}'.format('sex_pharm_subtype','png'))
# plt.show()
# plt.close()

# sys.exit()
#####################################################################################################################################################

# 分别对以下列（分类变量）绘制hist plot: iq, age, adhdpr1, adhdpr, atScoreP, atRatioP, hiScoreP, hiRatioP, adhdtr1, adhdtr, atScoreT, atRatioT, hiScoreT, hiRatioT
def drawHist(colname,groupnumber):
    col_value=data[colname].dropna().sort_values().values
    # print(col_value)
    plt.hist(col_value,groupnumber)
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug_new'+os.sep+'{}.{}'.format(colname,'png'))
    plt.show()
    plt.close()

# hist绘制时有一个特殊的地方在于不同的变量对应分的组别不一致，所以可能要衡量写循环时候怎么写

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

########################################################################################################################################
# adhdpr1, adhdpr, atScoreP, atRatioP, hiScoreP, hiRatioP, adhdtr1, adhdtr, atScoreT, atRatioT, hiScoreT, hiRatioT
# groupby sex, subtype, pharm
def drawSubBar(colname,subname,kind):
    # data.groupby([colname,subname])[[colname,subname]].count().unstack().plot(kind=kind,stacked=True)#各自分布的叠加
    data.groupby([colname, subname])[[colname]].count().unstack().plot(kind=kind, stacked=True) # colname分布为基础，subname中不同类别的分布是否一致
    # print(col_value)
    plt.xlabel('{}'.format(colname))
    plt.ylabel('Frequency')
    plt.title('distribution in all samples')
    plt.legend(loc='best')
    plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug_new'+os.sep+'{}_{}_{}.{}'.format(colname,subname,kind,'png'))
    plt.show()
    plt.close()

# plotkind=['bar','line']
# for name in colnamelist:
#     for sub in subnamelist:
#         for style in plotkind:
#             drawSubBar(colname=name,subname=sub,kind=style)

###############################################################################################################################################################
# plot sub plot in one picture
def drawSubBarOne(colname,subname,ax):
    data.groupby([colname, subname])[[colname]].count().unstack().plot(kind='bar',stacked=True,ax=ax)
    ax.set_xlabel('{}'.format(colname))
    ax.set_ylabel('Frequency')
    ax.set_title('{}''{}'.format(subname,' distribution in all samples'))
    ax.legend(loc='best')#在合适的位置放置图例

# colnamelist=['adhdpr']# for test
for name in colnamelist:
    fig2=plt.figure(figsize=(30,10))
    n = 1
    for sub in subnamelist:
        ax = fig2.add_subplot(1, 3, n)
        print()
        drawSubBarOne(colname=name,subname=sub,ax=ax)
        n=n+1
        ax = plt.gca()  # 获取当前的坐标轴，gca=get current axis，之后对坐标轴字体等操作都是在ax基础上进行的，因为一般不直接对plt设置属性
        ax.xaxis.set_major_locator(xmajorLocator)
        ax.xaxis.set_minor_locator(xminorLocator)
        for ind, label in enumerate(ax.yaxis.get_ticklabels()):
            if ind % 8 == 0:  # every 10th label is kept
                label.set_visible(True)
            else:
                label.set_visible(False)

    # plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig\drug_new' + os.sep + '{}_{}.{}'.format(name,'sex_pharm_subtype','png'))
    plt.show()
    plt.close()

