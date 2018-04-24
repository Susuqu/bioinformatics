# GitHub related information
- ### qususu
- ### 2018/04/24
- ### Aim：

 ---
## 准备工作
- 首先，在GitHub官网为自己创建一个GitHub账号吧；
- 其次，如果想将本地local的文件实时推送到GitHub的仓储上，那么需要：
	- 先在本地安装git bash for windows；
	- 安装好git之后，对于文件的同步（fectch，pull，push等）可以通过多种方式完成，这里主要介绍两种我在使用的：
		- GitHub Desktop客户端（简单易操作）；
		- pycharm（使用稍微繁琐一点，但因为我们通常需要写python脚本&对脚本注释，所以如果能直接将pycharm和GitHub建立联系那么就很方便）；

## 通过GitHub Desktop客户端建立仓储、连接GitHub、pull、push等操作
这个比较简单，暂时先不写了。
- 蓝色标识是提示你会作为改变的文本被保存的，不要就点击一下。
- 绿色标识表示修改的内容。
- 红色标识表示删除。
- Summary就是这次改动的总结，我们也可以理解为标题（必填），而Description可以理解为详细更改内容（选填）

## 通过pycharm建立仓储、连接GitHub、pull、push等操作
简书上有一个教程写的还蛮清楚的，可以供参考：[pycharm连接github](https://www.jianshu.com/p/231584cb735b)
主要是今天演示了一遍如何使用，但依然不怎么熟练，趁着还有记忆先写一下总结一些需要注意的点：

### 今天get了pycharm使用的一些小技巧，所以对新“认知”先专门放在这里记录下：
- 可以直接open 一个GitHub来建立一个仓储；
- 可以通过建立一个requirements.txt文件，而该文件里存放了package的名字，那么pycharm就可以去自动检查是否安装了该包，然后如果没有就直接为你安装这些包；
- 一般针对每一个项目，最好通过建立python的虚拟环境作为解释器（那个vitural在哪里选来着？？？）；
- pycharm可以新建仓储，然后直接将整个仓储share到GitHub上；
- 也可以先fetch 一个已经在GitHub上建立好的仓储到local，然后在pycharm里编辑；
- 但pycharm不能对一个新文件（之前毫无关系的）推送到一个已经建立好的仓储上；

推荐的其他帖子，还没来得及看呢，有时间的时候希望看下：
[Git 12 岁了，为你送上 12 个 Git 的使用技巧！](https://www.oschina.net/translate/12-git-tips-gits-12th-birthday?lang=chs)

