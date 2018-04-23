---
style: candy
---

CNN basic knowledges
==========
Record of some key notes by **QuSusu**.
Some statements were directly copy from others.
Start at 2018/04/23, last update at 2018/04/23.

----
**所谓卷积神经网络，就是会自动的对于一张图片学习出最好的卷积核以及这些卷积核的组合方式，也就是对于一张图片的任务来说，求出最好的图片对于本任务的特征的表达，然后来进行判断** 

[知乎：能否对卷积神经网络工作原理做一个直观的解释？](https://www.zhihu.com/question/39022858)



一般在我们进行一个CNN训练的时候，会涉及到两大类参数：超参数（Hyperparameters）和参数（）。
超参数（Hyperparameters）：是我们根据经验人工给定的值。
参数（parameters）：是通过学习训练改变得到的值。
两大类参数分别具体包括哪些过程的哪些值、如何给定这些值一个初始值、偏好值、以及


| 过程 | 超参数 | 如何给定对应的初始值？ | 偏好值 | 举例 | F0 | G0 |
|---|---|---|---|---|---|---|
| 卷积 | 卷积层数 | 人工给定 | 好像没有偏好值 | E1 | F1 | G1 |
|   | 卷积核大小 | 人工给定 | 奇数 | E2 | F2 | G2 |
|   | 特定卷积层对应的输出数量 | 人工给定 | D3 | E3 | F3 | G3 |
| 池化 | 池化层数 | C4 | D4 | E4 | F4 | G4 |
|   | 池化后的输出大小 | C3 | D3 | E3 | F3 | G3 |
| Relu | Relu的次数 | C3 | D3 | E3 | F3 | G3 |
| 全连接 | 全连接的次数 | C3 | D3 | E3 | F3 | G3 |
| 其他 | stride | C4 | D4 | E4 | F4 | G4 |
|   | padding | C4 | D4 | E4 | F4 | G4 |

一个例子：
![一个卷积过程说明的例子]($res/%E4%B8%80%E4%B8%AA%E5%8D%B7%E7%A7%AF%E8%BF%87%E7%A8%8B%E8%AF%B4%E6%98%8E%E7%9A%84%E4%BE%8B%E5%AD%90.png)





如何给定对应的值？


超参数——Hyperparameters——根据经验人工给定的
参数——parameter——

