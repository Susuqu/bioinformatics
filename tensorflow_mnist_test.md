#Tensorflow
---
### - I: mnist test (一个经典案例)
### - 2018/04/20
### - QuSusu
### - To understand what is CNN and how to use Tensorflow complete CNN. 
### - Reference on:[ChenYuelong's Example](ChenYuelong "https://chenyuelong.github.io/tensorflow_learn/mnist_test.html")
---


## 对于步长选择的理解：
可以对比下，两种步长0.1，0.01 的情况下预测准确率的差别，比如步长是0.1时，那么永远也达不到最优化的准确性效果（这就相当于A和B之间距离实际为0.2m，但是B每一步都要走1m，而且方向都是朝着一个距离在走，所以无论B走多少次，B和A直接的距离都无法最接近真实值）。不过一般推荐步长是：0.01~0.0001。

	e.g.：
	train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

		ssh://qususu@192.168.13.160:22/Bioinfo/MDDRD2/PMO/qususu/venv_python/ngs/bin/python3 -u /Bioinfo/MDDRD2/PMO/qususu/python/AI/mnist_test_qu.py
		Successfully downloaded train-images-idx3-ubyte.gz 9912422 bytes.
		Extracting MNIST_data/train-images-idx3-ubyte.gz
		Successfully downloaded train-labels-idx1-ubyte.gz 28881 bytes.s
		Extracting MNIST_data/train-labels-idx1-ubyte.gz
		Successfully downloaded t10k-images-idx3-ubyte.gz 1648877 bytes.
		Extracting MNIST_data/t10k-images-idx3-ubyte.gz
		Successfully downloaded t10k-labels-idx1-ubyte.gz 4542 bytes.
		Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
		2018-04-20 13:51:13.935272: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2
		迭代次数为0,准确性为：0.2863
		迭代次数为500,准确性为：0.9091
		迭代次数为1000,准确性为：0.9020
		迭代次数为1500,准确性为：0.9160
		迭代次数为2000,准确性为：0.9140
		迭代次数为2500,准确性为：0.9068
		迭代次数为3000,准确性为：0.9172
		迭代次数为3500,准确性为：0.9217
		迭代次数为4000,准确性为：0.9091
		迭代次数为4500,准确性为：0.9200
		迭代次数为5000,准确性为：0.9056
		迭代次数为5500,准确性为：0.9205
		迭代次数为6000,准确性为：0.9142
		迭代次数为6500,准确性为：0.9143
		迭代次数为7000,准确性为：0.9221
		迭代次数为7500,准确性为：0.9143
		迭代次数为8000,准确性为：0.9228
		迭代次数为8500,准确性为：0.9036
		迭代次数为9000,准确性为：0.9211
		迭代次数为9500,准确性为：0.9110
		迭代次数为10000,准确性为：0.9159
		迭代次数为10500,准确性为：0.9231
		迭代次数为11000,准确性为：0.9174
		迭代次数为11500,准确性为：0.9217
		迭代次数为12000,准确性为：0.9211
		迭代次数为12500,准确性为：0.9194
		迭代次数为13000,准确性为：0.9147
		迭代次数为13500,准确性为：0.9195
		迭代次数为14000,准确性为：0.9228
		迭代次数为14500,准确性为：0.9199
		迭代次数为15000,准确性为：0.9142
		迭代次数为15500,准确性为：0.9152
		迭代次数为16000,准确性为：0.9233
		迭代次数为16500,准确性为：0.9197
		迭代次数为17000,准确性为：0.9251
		迭代次数为17500,准确性为：0.9176
		迭代次数为18000,准确性为：0.9128
		迭代次数为18500,准确性为：0.9200
		迭代次数为19000,准确性为：0.9133
		迭代次数为19500,准确性为：0.9197
		
		Process finished with exit code 0


	train_step=tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

		2018-04-20 14:01:21.919178: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2
		迭代次数为0,准确性为：0.3271
		迭代次数为500,准确性为：0.0980
		迭代次数为1000,准确性为：0.0980
		迭代次数为1500,准确性为：0.0980
		迭代次数为2000,准确性为：0.0980
		迭代次数为2500,准确性为：0.0980
		迭代次数为3000,准确性为：0.0980
		迭代次数为3500,准确性为：0.0980
		迭代次数为4000,准确性为：0.0980
		迭代次数为4500,准确性为：0.0980
		迭代次数为5000,准确性为：0.0980
		迭代次数为5500,准确性为：0.0980
		迭代次数为6000,准确性为：0.0980
		迭代次数为6500,准确性为：0.0980
		迭代次数为7000,准确性为：0.0980
		迭代次数为7500,准确性为：0.0980
		迭代次数为8000,准确性为：0.0980
		迭代次数为8500,准确性为：0.0980
		迭代次数为9000,准确性为：0.0980
		迭代次数为9500,准确性为：0.0980
		迭代次数为10000,准确性为：0.0980
		迭代次数为10500,准确性为：0.0980
		迭代次数为11000,准确性为：0.0980
		迭代次数为11500,准确性为：0.0980
		迭代次数为12000,准确性为：0.0980
		迭代次数为12500,准确性为：0.0980
		迭代次数为13000,准确性为：0.0980
		迭代次数为13500,准确性为：0.0980
		迭代次数为14000,准确性为：0.0980
		迭代次数为14500,准确性为：0.0980
		迭代次数为15000,准确性为：0.0980
		迭代次数为15500,准确性为：0.0980
		迭代次数为16000,准确性为：0.0980
		迭代次数为16500,准确性为：0.0980
		迭代次数为17000,准确性为：0.0980
		迭代次数为17500,准确性为：0.0980
		迭代次数为18000,准确性为：0.0980
		迭代次数为18500,准确性为：0.0980
		迭代次数为19000,准确性为：0.0980
		迭代次数为19500,准确性为：0.0980
		
	

## 对于每次迭代准确性不同的的理解：
因为初始值是随机的，所以结果不同，但是如果训练到最后，应该相差不大。


## linux下交互型来每次看下定义了什么、输出什么，更便于理解：
	sess =tf.InteractiveSession()
	sess.run(init)
	a.eval()

---

## some questions
占位符的个数，就是指x像素点的个数么？——yes
	
	x = tf.placeholder(tf.float32, [None, 784])


trained+test的数据集都读进来了吗？——yes
	
	mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

这个是指：将所有的数据集随机分成不同的batch，每个batch包含了128张图片，每次读取一个batch的图片；sess.run读取数据集的方式就是必须写成dict的形式；
	
	batch_xs, batch_ys = mnist.train.next_batch(batch_size=128,shuffle=True)

	acc = sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})


为啥要传入这个？——为了后续的参数调整时，变化量很小时不会因为梯度推回而损失特征。

	keep_prob = tf.placeholder(tf.float32,name='keep_prob')

还是不清楚那个plt一张图片怎么显示啊？——plt.imshow???明天实验一下。
	
	MNIST_data：这下面的4个文件是4张片子——不是啊啊


因为传入的数据为转好的列向量，需要将他转化成矩阵的形式
	
	x_image = tf.reshape(cnn_x, [-1, 28, 28, 1])