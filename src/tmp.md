# MNIST test results & bug recored:
### 迭代次数为20000，想尝试print('迭代次数为%05d,准确性为：%.4f'%(i,acc)) 输出对齐，但结果报错；
    E:\OuMengCompany\Project\git\temp\venv\Scripts\python.exe E:/OuMengCompany/Project/git/temp/bioinform/src/mnist_test_qu.py
    Extracting MNIST_data/train-images-idx3-ubyte.gz
    Extracting MNIST_data/train-labels-idx1-ubyte.gz
    Extracting MNIST_data/t10k-images-idx3-ubyte.gz
    Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
    2018-04-28 12:20:48.910905: I C:\tf_jenkins\workspace\rel-win\M\windows\PY\36\tensorflow\core\platform\cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX
    迭代次数为00000,准确性为：0.1549
    迭代次数为00500,准确性为：0.9081
    迭代次数为01000,准确性为：0.9012
    迭代次数为01500,准确性为：0.9208
    迭代次数为02000,准确性为：0.9164
    迭代次数为02500,准确性为：0.9202
    迭代次数为03000,准确性为：0.8964
    迭代次数为03500,准确性为：0.9204
    迭代次数为04000,准确性为：0.9086
    迭代次数为04500,准确性为：0.9151
    迭代次数为05000,准确性为：0.9180
    迭代次数为05500,准确性为：0.9218
    迭代次数为06000,准确性为：0.9233
    迭代次数为06500,准确性为：0.9194
    迭代次数为07000,准确性为：0.9198
    迭代次数为07500,准确性为：0.9003
    迭代次数为08000,准确性为：0.9235
    迭代次数为08500,准确性为：0.9255
    迭代次数为09000,准确性为：0.9174
    迭代次数为09500,准确性为：0.9082
    迭代次数为10000,准确性为：0.9218
    迭代次数为10500,准确性为：0.9172
    迭代次数为11000,准确性为：0.9152
    迭代次数为11500,准确性为：0.9264
    迭代次数为12000,准确性为：0.9210
    迭代次数为12500,准确性为：0.9167
    迭代次数为13000,准确性为：0.9218
    迭代次数为13500,准确性为：0.9218
    迭代次数为14000,准确性为：0.9193
    迭代次数为14500,准确性为：0.9233
    迭代次数为15000,准确性为：0.9149
    迭代次数为15500,准确性为：0.9150
    迭代次数为16000,准确性为：0.9203
    迭代次数为16500,准确性为：0.9224
    迭代次数为17000,准确性为：0.9202
    迭代次数为17500,准确性为：0.9104
    迭代次数为18000,准确性为：0.9196
    迭代次数为18500,准确性为：0.9185
    迭代次数为19000,准确性为：0.9164
    迭代次数为19500,准确性为：0.9181
    Extracting MNIST_data/train-images-idx3-ubyte.gz
    Extracting MNIST_data/train-labels-idx1-ubyte.gz
    Extracting MNIST_data/t10k-images-idx3-ubyte.gz
    Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
    迭代次数为00000,准确性为：0.1333
    迭代次数为00500,准确性为：0.8362
    迭代次数为01000,准确性为：0.8837
    迭代次数为01500,准确性为：0.9080
    迭代次数为02000,准确性为：0.9219
    迭代次数为02500,准确性为：0.9288
    迭代次数为03000,准确性为：0.9348
    迭代次数为03500,准确性为：0.9402
    迭代次数为04000,准确性为：0.9428
    迭代次数为04500,准确性为：0.9457
    迭代次数为05000,准确性为：0.9483
    迭代次数为05500,准确性为：0.9514
    迭代次数为06000,准确性为：0.9523
    迭代次数为06500,准确性为：0.9545
    迭代次数为07000,准确性为：0.9559
    迭代次数为07500,准确性为：0.9570
    迭代次数为08000,准确性为：0.9586
    迭代次数为08500,准确性为：0.9590
    迭代次数为09000,准确性为：0.9597
    迭代次数为09500,准确性为：0.9610
    迭代次数为10000,准确性为：0.9622
    迭代次数为10500,准确性为：0.9620
    迭代次数为11000,准确性为：0.9631
    迭代次数为11500,准确性为：0.9644
    迭代次数为12000,准确性为：0.9657
    迭代次数为12500,准确性为：0.9659
    迭代次数为13000,准确性为：0.9672
    迭代次数为13500,准确性为：0.9673
    迭代次数为14000,准确性为：0.9678
    迭代次数为14500,准确性为：0.9689
    迭代次数为15000,准确性为：0.9687
    迭代次数为15500,准确性为：0.9694
    迭代次数为16000,准确性为：0.9692
    迭代次数为16500,准确性为：0.9705
    迭代次数为17000,准确性为：0.9703
    迭代次数为17500,准确性为：0.9713
    迭代次数为18000,准确性为：0.9711
    迭代次数为18500,准确性为：0.9723
    迭代次数为19000,准确性为：0.9723
    迭代次数为19500,准确性为：0.9730
    Traceback (most recent call last):
      File "E:/OuMengCompany/Project/git/temp/bioinform/src/mnist_test_qu.py", line 145, in <module>
        data.plot(x='times',xlim=(0,20000),ylim=(0,1),titile='compare linear with cnn')
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\pandas\plotting\_core.py", line 2677, in __call__
        sort_columns=sort_columns, **kwds)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\pandas\plotting\_core.py", line 1902, in plot_frame
        **kwds)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\pandas\plotting\_core.py", line 1729, in _plot
        plot_obj.generate()
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\pandas\plotting\_core.py", line 252, in generate
        self._make_plot()
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\pandas\plotting\_core.py", line 977, in _make_plot
        **kwds)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\pandas\plotting\_core.py", line 993, in _plot
        lines = MPLPlot._plot(ax, x, y_values, style=style, **kwds)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\pandas\plotting\_core.py", line 607, in _plot
        return ax.plot(*args, **kwds)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\__init__.py", line 1855, in inner
        return func(ax, *args, **kwargs)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\axes\_axes.py", line 1527, in plot
        for line in self._get_lines(*args, **kwargs):
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\axes\_base.py", line 406, in _grab_next_args
        for seg in self._plot_args(this, kwargs):
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\axes\_base.py", line 396, in _plot_args
        seg = func(x[:, j % ncx], y[:, j % ncy], kw, kwargs)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\axes\_base.py", line 300, in _makeline
        seg = mlines.Line2D(x, y, **kw)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\lines.py", line 421, in __init__
        self.update(kwargs)
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\artist.py", line 888, in update
        for k, v in props.items()]
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\artist.py", line 888, in <listcomp>
        for k, v in props.items()]
      File "E:\OuMengCompany\Project\git\temp\venv\lib\site-packages\matplotlib\artist.py", line 881, in _update_property
        raise AttributeError('Unknown property %s' % k)
    AttributeError: Unknown property titile

    Process finished with exit code 1


print('迭代次数为%05d,准确性为：%.4f'%(i,acc)) #在猜测是不是因为这个报错了；结果出来了可是没有绘图；
其实是data.plot(x='times',xlim=(0,3000),ylim=(0,1),title='compare linear with cnn')这里的titile拼写错误了！！！
准备再试下
本地运行速度实在是太慢了，所以改成迭代词素为3000再次运行了一下，主要是想找到出错的原因在哪里。

### 迭代次数为3000运行出来的结果，成功汇出图来了。
    E:\OuMengCompany\Project\git\temp\venv\Scripts\python.exe E:/OuMengCompany/Project/git/temp/bioinform/src/mnist_test_qu.py
    Extracting MNIST_data/train-images-idx3-ubyte.gz
    Extracting MNIST_data/train-labels-idx1-ubyte.gz
    Extracting MNIST_data/t10k-images-idx3-ubyte.gz
    Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
    2018-05-01 10:22:12.183318: I C:\tf_jenkins\workspace\rel-win\M\windows\PY\36\tensorflow\core\platform\cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX
    迭代次数为0,准确性为：0.4787
    迭代次数为500,准确性为：0.9053
    迭代次数为1000,准确性为：0.9187
    迭代次数为1500,准确性为：0.9182
    迭代次数为2000,准确性为：0.9138
    迭代次数为2500,准确性为：0.9100
    Extracting MNIST_data/train-images-idx3-ubyte.gz
    Extracting MNIST_data/train-labels-idx1-ubyte.gz
    Extracting MNIST_data/t10k-images-idx3-ubyte.gz
    Extracting MNIST_data/t10k-labels-idx1-ubyte.gz
    迭代次数为0,准确性为：0.0877
    迭代次数为500,准确性为：0.8093
    迭代次数为1000,准确性为：0.8803
    迭代次数为1500,准确性为：0.9079
    迭代次数为2000,准确性为：0.9232
    迭代次数为2500,准确性为：0.9315

    Process finished with exit code 0

![迭代次数为3000时线性和cnn的结果对比图](../images/compare_linear_with_cnn_1.PNG)

看不出来cnn明显优于线性学习的效果，准备再试下15000，反正放假，提交了让它自己跑着吧。