# 质因数分解

from math import sqrt

global prime
prime = [2,3,5,7] # 质数列表

# 列表更新
def update():
    global prime
    num = prime[-1] + 1
    num = find_pri(num)
    prime.append(num)
    return num


# 查找质数
def find_pri(num):
    i = num
    while True:
        j,k = 2,int(sqrt(i))+1
        while j <= k:
            if j == k:
                return i
            if (i%j) == 0:
                break
            j += 1
        i += 1     


# 查找因子
def find_div(num,pri):
    index = prime.index(pri)
    for i in range(index,len(prime)):
        pri = prime[i]
        if (num % pri) == 0:
            return pri
    while (num % pri) != 0:
        pri = update()
    return pri


# 分解质因数
def resolve(num):
    arr = [] # 质因数
    pri = 2  # 质数
    while num != 1:
        pri = find_div(num,pri)
        num = num / pri
        arr.append(pri)
    return arr        


# 展示分解过程
def show(num,arr):
    arr.sort(reverse=False)
    print('%d = '%(num),end='')
    print(' * '.join(map(str,arr)))


while True:
    opt = input('待分解整数（q退出）：')
    if opt == 'q':
        break
    if opt == 'p':
        print(prime)
        continue
    num = int(opt)
    arr = resolve(num)
    show(num,arr) # 打印结果
