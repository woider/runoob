'''
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
'''

from math import sqrt

min = 101
max = 200

prime = list()

for i in range(min,max+1):
    temp = int(sqrt(i))
    flag = True # 是否为素数
    for j in range(2,temp+1):
        if (i%j) == 0:
            flag = False
            break
    if flag == True:
        prime.append(i)

print('%d-%d 之间共有 %d 个素数'%(min,max,len(prime)))
print(prime)
