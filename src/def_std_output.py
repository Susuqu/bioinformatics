# -*-coding:utf-8 -*-

'''
ref:
    https://blog.csdn.net/gatieme/article/details/45439671
    https://btrspg.github.io/2018/05/22/python-output-color/

希望在终端上输出一些带有颜色或者粗体、下划线等样式的信息，从而快速的根据颜色更好的区分不同的结果。python标准输出的两种方法：
    1.直接调用python 包: colorama；
    2.自己定义一个方法；
    注：两种方法在Windows下想终端显示颜色需要加：init(wrap=False)。
'''

## 方法一
# pip install colorama 第一次使用需要安装
# colorama的官方说明文档：https://pypi.org/project/colorama/

from colorama import init, Fore, Back, Style

# 只有这些颜色可以选
# Fore：BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

if __name__ == '__main__':

    init(wrap=False)    #解决Windows下无法显示颜色的问题，但是这个参数不能和autoreset=True同时使用，The default behaviour is to wrap if autoreset or strip or convert are True.
    # init(autoreset=True)    #这一步就可以省去自己每次用完之后要重新reset的麻烦

    print(Fore.RED+'前景色为红色')
    print(Back.GREEN+'背景色为绿色')
    print(Style.BRIGHT+'模式为高亮')
    print(Style.DIM+'模式为DIM')
    print(Style.NORMAL+'模式为NORMAL')
    print(Fore.RED+Back.GREEN+Style.DIM+'前景色为红色，背景色为绿色')

########################################################################

## 方法二
def UseStyle(string, mode='',fore='',back=''):
    '''
    :param string: 需要特别输出的string
    :param mode: 输出模式
    :param fore: 前景色
    :param back: 背景色
    :return:
    '''
    STYLE={
            'fore':
                    {#前景色
                    'black': 30, #黑色
                    'red': 31,  # 红色
                    'green': 32,  # 绿色
                    'yellow': 33,  # 黄色
                    'blue': 34,  # 蓝色
                    'purple': 35,  # 紫红色
                    'cyan': 36,  # 青蓝色
                    'white': 37,  # 白色
                    },

            'back':
                    {  # 背景
                    'black': 40,  # 黑色
                    'red': 41,  # 红色
                    'green': 42,  # 绿色
                    'yellow': 43,  # 黄色
                    'blue': 44,  # 蓝色
                    'purple': 45,  # 紫红色
                    'cyan': 46,  # 青蓝色
                    'white': 47,  # 白色
                    },

            'mode':
                    {  # 显示模式
                    'mormal': 0,  # 终端默认设置
                    'bold': 1,  # 高度显示
                    'underline': 4,  # 使用下划线
                    'blink': 5,  # 闪烁
                    'invert': 7,  # 反白显示
                    'hide': 8,  # 不可见
                    },

            'default':
                    {
                    'end':0,
                    },
             }

    # 判断key对应的值是否在dict中，值得注意的是，下面这种写法，传参时不能传入数值（比如闪烁对应的数值是5），而必须是对应的字符串（比如闪烁对应的字符串是'blink'）.
    # 因为‘blink’是key值，5是value值。查询的时候是根据key查。

    # 语法扫盲：
        # %s的作用：%s，他的含义是“这里将被替换成一个新的字符串”，那么第二个%后面的内容就是新的字符串内容；
        # 详细链接可以看：https://www.zhihu.com/question/54933434

    mode='%s' % STYLE['mode'][mode] if mode in STYLE['mode'].keys() else ''
    fore='%s' % STYLE['fore'][fore] if fore in STYLE['fore'].keys() else ''
    back='%s' % STYLE['back'][back] if back in STYLE['back'].keys() else ''

    style=';'.join([s for s in [mode,fore,back] if s])
    style='\033[%sm' % style if style else ''

    # 加end就是为了将设置重新设回default
    end= '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style,string,end)

# print(UseStyle('这是什么颜色',mode=1,fore=33,back=43))

def TestColor( ):
    print (UseStyle('正常显示'))
    print ('')

    print ("测试显示模式")
    print (UseStyle('高亮',   mode = 'bold')),
    print (UseStyle('下划线', mode = 'underline')),
    print (UseStyle('闪烁',   mode = 'blink')),
    print (UseStyle('反白',   mode = 'invert')),
    print (UseStyle('不可见', mode = 'hide'))
    print ('')

    print ("测试前景色")
    print (UseStyle('黑色',   fore = 'black')),
    print (UseStyle('红色',   fore = 'red')),
    print (UseStyle('绿色',   fore = 'green')),
    print (UseStyle('黄色',   fore = 'yellow')),
    print (UseStyle('蓝色',   fore = 'blue')),
    print (UseStyle('紫红色', fore = 'purple')),
    print (UseStyle('青蓝色', fore = 'cyan')),
    print (UseStyle('白色',   fore = 'white'))
    print ('')

    print ("测试背景色")
    print (UseStyle('黑色',   back = 'black')),
    print (UseStyle('红色',   back = 'red')),
    print (UseStyle('绿色',   back = 'green')),
    print (UseStyle('黄色',   back = 'yellow')),
    print (UseStyle('蓝色',   back = 'blue')),
    print (UseStyle('紫红色', back = 'purple')),
    print (UseStyle('青蓝色', back = 'cyan')),
    print (UseStyle('白色',   back = 'white'))
    print ('')

if __name__ == '__main__':

    TestColor()