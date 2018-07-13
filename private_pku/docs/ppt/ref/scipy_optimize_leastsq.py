# -*- coding:utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib
zhfont1=matplotlib.font_manager.FontProperties(fname=r'C:\Windows\Fonts\MSYH.TTC')#否则legend无法显示中文字体

#最小二乘拟合,optimize已经提供了实现最小二乘拟合算法的函数leastsq
#首先构造一个正弦波函数，然后y0是原始值，y1是通过y0构造出来的噪音值，最小二乘拟合的目的就是找是的y1-y0最小差值的p
def func(x,p):
    A,k,theta=p
    return A*np.sin(2*np.pi*k*x+theta)
def residuals(p,y,x):
    return y-func(x,p)

x=np.linspace(0,-2*np.pi,100)
A,k,theta=10,0.34,np.pi/6
y0=func(x,[A,k,theta])
y1=y0+2*np.random.rand(len(x))

p0=[7,0.2,0]#给定参数的初始化值

plsq=leastsq(residuals,p0,args=(y1,x))
print("真实参数：",[A,k,theta])
print("拟合参数：",plsq[0])

pl.plot(x,y0,label=u'真实数据')
pl.plot(x,y1,label=u"带噪声的实验数据")
pl.plot(x,func(x,plsq[0]),label=u"拟合数据")
#pl.legend([u"真实数据",u"带噪声的实验数据",u"拟合数据"])
pl.legend(prop=zhfont1)
pl.show()
