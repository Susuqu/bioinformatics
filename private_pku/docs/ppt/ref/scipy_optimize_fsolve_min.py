# -*- coding:utf-8 -*-
import numpy as np
from scipy import optimize  # 优化和拟合
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from math import sin,cos

#用scipy.optimize中的算数来求最小值
def f(x):
    return x ** 2 + 10 * np.sin(x)

x = np.arange(-10, 10, 0.1)
plt.plot(x, f(x))
plt.show()

print(optimize.fmin_bfgs(f, 0))
# optimize.fmin_bfgs(f,3,disp=0)

#不加预判的情况下求全局的最小值
grid = (-10, 10, 0.1)
xmin_global = optimize.brute(f, (grid,))
print(xmin_global)

#求局部最小值
xmin_local = optimize.fminbound(f, 0, 10)
print(xmin_local)

#print(dir(norm))#看下norm对应都有哪些函数属性

#非线性方程组求解，optimize中的fsolve函数
    # fsolve(func,x0)

    # f1(u1,u2,u3)=0
    # f2(u1,u2,u3)=0
    # f3(u1,u2,u3)=0
    #
    # def func(x):
    #     u1,u2,u3=x
    #     return [f1(u1,u2,u3),f2(u1,u2,u3),f3(u1,u2,u3)]
    #

# 求解如下方程组的解
# 5*x1+3=0
# 4*x0*x0-2*sin(x1*x2)=0
# x1*x2-1.5=0

def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
        5 * x1 + 3,
        4 * x0 * x0 - 2 * sin(x1 * x2),
        x1 * x2 - 1.5
    ]
result = fsolve(f, [1, 1, 1])

print(result)
print(f(result))

