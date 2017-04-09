'''
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。
'''

# 分解质因数
def resolve(num):
    arr = [] # 质因数
    pri = 2  # 质数
    print('%d = '%(num),end='')
    while pri != num:
        if (num % pri) == 0:
            arr.append(pri)
            num = num/pri
            continue
        pri = prime(pri)
    arr.append(pri)
    print(' * '.join(map(str,arr)))

# 质数生成器
def prime(num):
    i = num + 1
    while True:
        j = 2
        while j <= i:
            if i == j:
                return i
            if (i%j) == 0:
                break
            j += 1
        i += 1

while True:
    opt = input('待分解整数（q退出）：')
    if opt == 'q':
        break
    num = int(opt)
    resolve(num)