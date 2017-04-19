# 条件判断

age = 3
if age >= 18:
    print('your age is',age)
    print('adult')
elif age >= 6:
    print('your age is',age)
    print('teenager')
else:
    print('kid')


if not (tuple() or '' or 0 or []):
    print('非零数值、非空字符串、非空list判断为True')


# 练习

height = 1.75
weight = 80.5

rate = weight / (height * height)

if rate < 18.5:
    print('过轻')
elif rate < 25:
    print('正常')
elif rate < 28:
    print('过重')
elif rate < 32:
    print('肥胖')
else:
    print('过于肥胖')
