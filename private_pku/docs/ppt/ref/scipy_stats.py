# -*- coding:utf-8 -*-
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

#直方图和概率密度曲线
a = np.random.normal(size=1000)
print(a,end=',')
bins = np.arange(-4, 5)
print(bins)
histogram = np.histogram(a, bins=bins, normed=True)[0]
bins = 0.5 * (bins[1:] + bins[:-1])
print(bins)

b = stats.norm.pdf(bins)#对拟合出来的正态分布绘制对应的概率密度曲线
plt.plot(bins, histogram)
plt.plot(bins, b)
plt.show()

# 百分位,百分位是CDF的一个估计器(累积分布函数)。
print(np.median(a))
print(stats.scoreatpercentile(a, 50))
print(stats.scoreatpercentile(a, 90))

# 统计检验
c = np.random.normal(0, 1, size=100)
d = np.random.normal(1, 1, size=10)
print(stats.ttest_ind(c, d))
