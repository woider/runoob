'''
题目：格式化输出当前时间。

程序分析：%Y 带世纪部分的十制年份，%m 十进制表示的月份，%d 十进制表示的每月的第几天，%H 24小时制的小时，%M 十时制表示的分钟数，%S 十进制的秒数。
'''

import time

format = '%Y-%m-%d %H:%M:%S'
local = time.localtime(time.time())

print(time.strftime(format,local))
