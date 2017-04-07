'''
题目：将一个列表的数据复制到另一个列表中。

程序分析：使用列表[:]。
'''

origin = ['javascript','php','python']

refer  = origin

copy = origin[:]

print('origin(%x): %s' % (id(origin),str(origin)))

print('refer(%x): %s' % (id(refer),str(refer)))

print('copy(%x): %s' % (id(copy),str(copy)))
