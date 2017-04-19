# for循环

sum = 0
for x in range(1,101):
    sum += x

print(sum)


# while循环

sum = 0
n = 99

while n > 0:
    sum += n
    n = n - 2

print(sum)


# 练习

L = ['Bart','Lisa','Adam']

for i in L:
    print('Hello,%s'%(i))


# break

n = 0
while True:
    if n == 3:
        break
    print('提前结束循环')
    n += 1


# continue

n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(n,end=' ')


