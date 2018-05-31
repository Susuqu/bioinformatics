# -*-coding:utf-8 -*-
'''
在网上看到的一个很有意思的代码，就是在屏幕上打印出心形图案，感觉容易实现而且也有一些函数和语法可以学习，所以就试试
然后试了简单的例子发现网上还有3D打印的教程，就copy过来稍微调试了，会玩！
但依然有疑惑的点，明天再弄清楚细节哈~
# @Time     : 2018/05/30
# @Author   : Qu Susu

some questions:
1.看了一下这个代码，还是不懂为啥expression要这样定义？那么是不是我改变expression就可以改变形状？
2.range的范围是怎么取的？
3.3D图片打印那个，发现有个变量定义了但是根本没用到啊：cset
学会了一招新技能，关闭坐标轴的刻度：plt.axis('off')
'''
import sys
import time
from colorama import init, Fore, Back, Style
init(wrap=False) #这个刚好学以致用了！

words=input('Please input the words you want to say!:')
# eg: "Dear, Happy Valentine's Day! LiLei will always Love you till the end! Forever!"
# input的话其实就和perl的标准输入很像了
for item in words.split():
    letterlist=[]
    for y in range(12,-12,-2):
        list_X=[]
        letters=''
        for x in range(-30,30):
            expression=((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
            if expression <=0:
                letters+=item[(x-y)%len(item)]
            else:
                letters+=' '
        list_X.append(letters)
        letterlist+=list_X
    print(Fore.RED+'\n'.join(letterlist))
    time.sleep(1.5);

sys.exit
##################################################################################################################
#3D心形
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']    #这一行必须加，否则中文乱码的作用就无法实现

def heart_3d(x,y,z):
    return (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3


def plot_implicit(fn, bbox=(-1.5, 1.5)):
    xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    A = np.linspace(xmin, xmax, 100) # resolution of the contour
    B = np.linspace(xmin, xmax, 40) # number of slices
    A1, A2 = np.meshgrid(A, A) # grid on which the contour is plotted

    for z in B: # plot contours in the XY plane
        X, Y = A1, A2
        Z = fn(X, Y, z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z', colors=('r',))
        # [z] defines the only level to plot
        # for this contour for this value of z

    for y in B: # plot contours in the XZ plane
        X, Z = A1, A2
        Y = fn(X, y, Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y', colors=('red',))

    for x in B: # plot contours in the YZ plane
        Y, Z = A1, A2
        X = fn(x, Y, Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x',colors=('red',))

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level. Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.

    ax.set_zlim3d(zmin, zmax)
    ax.set_xlim3d(xmin, xmax)
    ax.set_ylim3d(ymin, ymax)
     #标题
    plt.title(u"把我的小心心送给你啊")
    # plt.axis('off')  #取消坐标轴显示
    plt.savefig(r"E:\OuMengCompany\Project\git\temp\bioinform\src\fig\3D_heart.png")
    plt.show()

if __name__ == '__main__':
    plot_implicit(heart_3d)