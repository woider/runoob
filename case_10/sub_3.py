'''
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

程序分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。
'''

import math

for i in range(10000):
    n = math.sqrt(i+100)
    m = math.sqrt(i+268)
    if n%1==0 and m%1==0:
        print(i)
    #print(m,n)
