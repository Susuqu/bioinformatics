# -*-coding:utf-8 -*-

##################################谁能告诉我？为啥我的没有颜色显示###################
# pip install colorama
from colorama import init, Fore, Back, Style

# 只有这些颜色可以选
# Fore：BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET
# Style: DIM, NORMAL, BRIGHT, RESET_ALL

if __name__ == '__main__':

    init(autoreset=True)    #这一步就可以省去自己每次用完之后要重新reset的麻烦
    print(Fore.RED+'前景色为红色')
    print(Back.GREEN+'背景色为绿色')
    print(Style.BRIGHT+'模式为高亮')
    print(Style.DIM+'模式为DIM')
    print(Style.NORMAL+'模式为NORMAL')
    print(Fore.RED+Back.GREEN+Style.DIM+'前景色为红色，背景色为绿色')


########################################################################

# 神奇的是竟然在输入'''时自动弹出来了中间的那些字符串，很省事啊
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
    # 原代码中使用的是STYLE['mode'].has_key(mode)
    # 这种写法是python2中的，python3中一般使用下面这种写法，判断key对应的值是否在dict中

    mode='%s' % STYLE['mode'][mode] if mode in STYLE['mode'].keys() else ''
    fore='%s' % STYLE['fore'][fore] if fore in STYLE['fore'].keys() else ''
    back='%s' % STYLE['back'][back] if back in STYLE['back'].keys() else ''

    style=';'.join([s for s in [mode,fore,back] if s])
    style='\033[%sm' % style if style else ''

    # 加end就是为了将设置重新设回default
    end= '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style,string,end)

print(UseStyle('这是什么颜色',mode=1,fore=33,back=43))