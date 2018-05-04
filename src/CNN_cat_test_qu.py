# -*-coding:utf-8 -*-
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import math

'''
一小组图像集可以表示为一个四维浮点数数组：[batch, height, width, channels]
'''

def weight_variable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial=tf.constant(0.1,shape=shape)
    return tf.Variable(initial)

def conv2d(x,W):
    return tf.nn.conv2d(input=x,filter=W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

def max_pool_3x3(x):
    return tf.nn.max_pool(x,ksize=[1,3,3,1],strides=[1,3,3,1],padding='SAME')

def max_pool_5x5(x):
    return tf.nn.max_pool(x,ksize=[1,5,5,1],strides=[1,5,5,1],padding='SAME')

def max_pool_15x15(x):
    return tf.nn.max_pool(x,ksize=[1,15,15,1],strides=[1,15,15,1],padding='SAME')

def relu(x):
    return tf.nn.relu(x)

#tf.nn = tensorflow.python.ops.nn

cat=tf.gfile.FastGFile('../images/cat.jpg','rb').read()
image=tf.image.decode_jpeg(cat)

with tf.Session() as sess:
    print(image.eval().shape)
    plt.figure(1)
    plt.imshow(image.eval())
    # plt.show()
#(741, 834, 3)

# 卷积大小从1*1 到10*10，分别变化后输出
def conv_test(image,batch):
    image=tf.cast(image,tf.float32)
    cat_batch=tf.reshape(image,[1,741,834,3])
    W=weight_variable([batch,batch,3,3])
    op=tf.nn.conv2d(cat_batch,W,strides=[1,1,1,1],padding='SAME',use_cudnn_on_gpu=False)
    conv=tf.reshape(tf.cast(op,tf.uint8),[741,834,3])
    return conv

mylist=[]
for i in range(10):
    n=i+1
    mylist.append(conv_test(image,n))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    n=0
    for i in mylist:
        n=n+1
        test=sess.run(i)
        plt.figure(n)
        plt.title('conv:{}'.format(n))
        plt.imshow(test)
        plt.savefig("n.png")
        # plt.show() #屏幕打印


# 卷积之后加入最大池化作用
def conv_max_test(image,batch):
    image=tf.cast(image,tf.float32)
    cat_batch = tf.reshape(image, [1, 741, 834, 3])
    W=weight_variable([batch,batch,3,3])
    op=tf.nn.conv2d(cat_batch,W,strides=[1,1,1,1],padding='SAME',use_cudnn_on_gpu=False)

    max_op_2x2=max_pool_2x2(op)
    max_op_3x3=max_pool_3x3(op)
    max_op_5x5=max_pool_5x5(op)
    max_op_15x15=max_pool_15x15(op)

    conv =tf.reshape(tf.cast(op,tf.uint8),[741,834,3])
    conv_max_2x2 = tf.reshape(tf.cast(max_op_2x2,tf.uint8),[math.ceil(741/2),math.ceil(834/2),3])
    conv_max_3x3 = tf.reshape(tf.cast(max_op_3x3,tf.uint8),[math.ceil(741/3),math.ceil(834/3),3])
    conv_max_5x5 = tf.reshape(tf.cast(max_op_5x5,tf.uint8),[math.ceil(741/5),math.ceil(834/5),3])
    conv_max_15x15 = tf.reshape(tf.cast(max_op_15x15,tf.uint8),[math.ceil(741/15),math.ceil(834/15),3])
    return conv,conv_max_2x2,conv_max_3x3,conv_max_5x5,conv_max_15x15

mylist = []
taglist = ['conv','2x2 max pool','3x3 max pool' ,'5x5 max pool','15x15 max pool']
for i in range(10):
    n=i+1
    mylist.append(conv_max_test(image,n))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    n=0
    for i in mylist:
        n=n+1
        test= sess.run(i)
        plt.figure(n, figsize=(20, 5), dpi=300)

        for j in range(5):
            ax=plt.subplot2grid((1,5),(0,j),colspan=1,rowspan=1)
            ax.set_title('{}:{}'.format(taglist[j], n), fontsize=8)
            ax.imshow(test[j])
            # plt.show()
'''
2018/05/04 suspend
'''