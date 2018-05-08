# -*-coding:utf-8 -*-

# @PROJECT  : ADHD
# @Time     : 2018/05/08
# @Author   : Qu Susu
# @Mail     : susu.qu@oumeng.com.cn
# @File     : sample_distribution_plot.py
# @Software : Pycharm

# pip install xlrd
import xlrd
import pandas as pd
import matplotlib.pyplot as plt
import os

# 读进xlsx文件，然后写入txt文本
def fileloadAndSave(filename):
    data=xlrd.open_workbook(filename)#打开Excel文件读取数据
    sheet=data.sheet_by_name("Sheet1")#通过工作簿名称获取
    print(sheet.nrows)#行数
    print(sheet.ncols)#列数
    n=0
    i=0
    file=open("tmp.txt","w")
    for n in range(sheet.nrows):
        for i in range(sheet.ncols):
            text=sheet.cell_value(n,i)
            file.write(str(text))
            file.write('\t')
        file.write('\n')
    file.close()
    return file

# def basicPlot(table):
table = pd.read_table("tmp.txt", encoding='gb2312')  # 不加encoding之前，真的是被折磨疯了！！！总是报错。然后还找不到报错原因，坑！
# encoding='gb2312':其他编码中文显示错误
print(table.columns)
print(table.index)
# print(table.head())
#这个地方画图是不是可以写个循环？
# 性别分布图
table["sex"].value_counts().plot(kind='bar')
plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig'+os.sep+'test_sex.png')
plt.show()
plt.close()

# 用药类别分布图
table["pham"].value_counts().plot(kind='bar')
plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig'+os.sep+'test_pham.png')
plt.show()
plt.close()

# age分布图
table["age"].value_counts().plot(kind='bar')
plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig'+os.sep+'test_age.png')
plt.show()
plt.close()

# iq分布图
table["iq"].value_counts().plot(kind='bar')
plt.savefig(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\fig'+os.sep+'test_iq.png')
plt.show()
plt.close()


# table["adhdt"].value_counts().sort_values().plot(kind='sca')
# plt.scatter(table["index"], table["adhdt"])
# plt.show()

def main():
    test=fileloadAndSave(r'E:\OuMengCompany\Project\ScientificResearchService\ADHD新样本性状分析\test.xlsx')
    # print(test,end='\n')

if __name__ == '__main__':
    main()

