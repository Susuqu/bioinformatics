# -*-coding:utf-8 -*-
# sess =tf.InteractiveSession()
# sess.run(init)
# a.eval()

import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

x=tf.placeholder(tf.float32,[None,784])
y_=tf.placeholder("float",[None,10])
# 28*28=784, but why is 28?
# why is 784? why x & y的数据type命名方式不同？

W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))
y=tf.nn.softmax(tf.matmul(x,W)+b)

cross_entropy=-tf.reduce_sum(y_*tf.log(y))
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,"float"))

init=tf.global_variables_initializer()


linear_list=[]
x_list=[]
mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)
with tf.Session() as sess:
    sess.run(init)
    for i in range(20000):
        batch_xs, batch_ys=mnist.train.next_batch(batch_size=128,shuffle=True)
        sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
        if i%500==0:
            x_list.append(i)
            acc=sess.run(accuracy,feed_dict={x:mnist.test.images,y_:mnist.test.labels})

            linear_list.append(acc)
            print('迭代次数为%d,准确性为：%.4f'%(i,acc))

# 3-CNN模型（网上示例）
# what's shape？
def weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

