# 字符串编码

'''
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码
'''

# Python 字符串

print('A:',ord('A'))
print('66:',chr(66))

print('\u4e2d\u6587')

print('中文'.encode('utf8'))
print(b'\xe7\xbc\x96\xe7\xa0\x81'.decode('utf8'))

print(len('字符串长度'))
print(len(b'\xe7\xbc\x96\xe7\xa0\x81'))

# 格式化
form = '整数(%d) 浮点数(%f) 字符串(%s) 十六进制(%x)'
print(form%(1024,3.1415926,'PI',id('IP')))

# 练习
s1 = 72
s2 = 85
r = ((s2-s1)/s1)*100

print('%.2f%%'%(r))
