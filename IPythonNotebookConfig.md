## 配置ipython notebook,解决远程无法访问、页面打不开的问题
查了网上很多教程才解决这个问题，记录一下。
[参考帖子CSDN-本地使用服务器端运行的Jupyter Notebook](https://blog.csdn.net/Papageno_Xue/article/details/79710708)

---
因为想使用ipython交互，并把交互的结果想直接保存为py脚本，就想用这个，然后就开始各种配了。

1.安装ipython notebook

2.启动notebook进行访问，如果无法访问就需要配置了

3.配置server使得在web输入网址可以访问ipython notebook

1）首先输入ipython生成秘钥

2）生成jupyter的config文件

3）修改配置文件：~/.jupyter/jupyter_notebook_config.py



在远程电脑上，打开浏览器，输入：