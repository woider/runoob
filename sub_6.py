'''
题目：斐波那契数列。

程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
'''

arr = [0, 1]

tmp,num = 0,1

dep = 20

for i in range(dep-2):
    tmp,num = num,tmp+num
    arr.append(num)

print(arr)
