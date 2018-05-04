# -*-coding:utf-8 -*-
'''
QuSusu
已测，没有问题，对应的结果记录和一些小问题在tensorflow_mnist_test.md文件中
'''
# sess =tf.InteractiveSession()
# sess.run(init)
# a.eval()
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

######################################################################
x=tf.placeholder(tf.float32,[None,784])
y_=tf.placeholder("float",[None,10])
# 28*28=784

W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
y=tf.nn.softmax(tf.matmul(x,W)+b)
#10表示有0-9，共10类图片

cross_entropy=-tf.reduce_sum(y_*tf.log(y))
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
#梯度递减

correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,"float"))
#真实值y_和训练得到的y之间的差值用来衡量模型的准确性

init=tf.global_variables_initializer()

######################################################################
linear_list=[]
x_list=[]
mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)
with tf.Session() as sess:
    sess.run(init)
    for i in range(15000):
        batch_xs, batch_ys=mnist.train.next_batch(batch_size=128,shuffle=True)
        sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
        if i%500==0:
            x_list.append(i)
            acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y_:mnist.test.labels})
            linear_list.append(acc)
            print('迭代次数为%d,准确性为：%.4f'%(i,acc))

'''
input_data.read_data_sets只是读进来数据，trained+test的数据集都读进来了
将所有的数据集随机分成不同的batch，每个batch包含了128张图片，每次读取一个batch的图片；sess.run读取数据集的方式就是必须写成dict的形式；

'''
######################################################################
# 3-CNN模型（网上示例）
def weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)
'''
忘了这个是干啥的了？是定义的卷积核的权重初始值么？——是，权重值的初始化
CNN里的W其实就是卷积核的大小和输入输出结果的个数
'''

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
#定义b的初始值

def conv2d(x,W):
    return tf.nn.conv2d(input=x,filter=W,strides=[1,1,1,1],padding='SAME')
#stride为啥是4个呢？

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

def relu(x):
    return tf.nn.relu(x)

def softmax(x):
    return tf.nn.softmax(x)

######################################################################
cnn_x=tf.placeholder(tf.float32,[None,784],name='cnn_x')
cnn_y=tf.placeholder(tf.float32,[None,10],name='cnn_y')
keep_prob=tf.placeholder(tf.float32,name='keep_prob') #主要是后续为了防止梯度消失用到了这个变量

x_image=tf.reshape(cnn_x,[-1,28,28,1])

# 第一层卷积+池化+relu
W_conv1=weight_variable([5,5,1,32])
b_conv1=bias_variable([32]) #因为卷积之后的输出结果有32个，所以b的个数也是对应的32个
h_conv1=relu(conv2d(x_image,W_conv1)+b_conv1)
h_pool1=max_pool_2x2(h_conv1) #output size 14x14x32

# 第二层卷积+池化+relu
W_conv2=weight_variable([5,5,32,64])
b_conv2=bias_variable([64])
h_conv2=relu(conv2d(h_pool1,W_conv2)+b_conv2)
h_pool2=max_pool_2x2(h_conv2) #output size 7x7x64

'''
全连接：经过卷积+池化+relu的过程之后，获得的还是很多矩阵的结果，全连接层就是将矩阵的结果转化而向我们之前做的扁平化的向量
例如有两张4x4的图片，其中一共包括32个像素点（4x4x2），相当于一个大小为[1,32]矩阵，经过全连接，我们可以用一个大小为[32,x]的矩阵去作用
那么这个原矩阵就的大小就会变成[1,x]，x可以为任意数，如下例子就是x=1024
'''
W_fc1=weight_variable([7*7*64,1024])
b_fc1=bias_variable([1024])
h_pool2_flat=tf.reshape(h_pool2,[-1,7*7*64]) #这一步没太懂为啥要对第二次池化后的结果reshape
h_fc1=relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1) #以及全连接为啥也是要relu呢？

## 为了防止梯度消失，会加入dropout
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
#为什么第二层这里就没有relu了呢？

prediction = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2)+ b_fc2)

cross_entropy = tf.reduce_mean(-tf.reduce_sum(cnn_y * tf.log(prediction),reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(1e-3).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(cnn_y,1), tf.argmax(prediction,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

init = tf.global_variables_initializer()

# 3-CNN模型（网上示例）运行及结果
mnist2=input_data.read_data_sets("MNIST_data/",one_hot=True)

cnn_list=[]
with tf.Session() as sess:
    sess.run(init)
    for i in range(15000):
        batch_xs,batch_ys=mnist2.train.next_batch(128)
        sess.run(train_step,feed_dict={cnn_x:batch_xs,cnn_y:batch_ys,keep_prob:0.5})##训练得到的y值
        if i%500==0:
            acc=sess.run(accuracy,feed_dict={cnn_x:mnist2.test.images,cnn_y:mnist2.test.labels,keep_prob:1})##test集合里的y（实际值）
            cnn_list.append(acc)
            print('迭代次数为%d,准确性为：%.4f'%(i,acc))

######################################################################
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(50,25),dpi=300)

data=pd.DataFrame([x_list,linear_list,cnn_list]).T
data.columns=['times','linear','cnn']

data.plot(x='times',xlim=(0,15000),ylim=(0,1),title='compare linear with cnn')
plt.show()

