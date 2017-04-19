# list

mates = ['Michael','Bob','Tracy']

print(mates[0],mates[1],mates[2])

def fmate():
    try:
        print(mates[3])
    except Exception:
        print('数组下标越界')
    else:
        print(mates[-1])
    finally:
        print(mates)

fmate()

mates.append('Adam')

fmate()

mates.insert(1,'Jack')

print(mates)

mates.pop()

print(mates)

s = ['c#','java',['asp','jsp','php'],'php']

s[0] = ['javascript','php','python']

print(s)


# tuple

mates = tuple(mates)

print(mates)

try:
    mates.pop()
except Exception as err:
    print(err)
finally:
    print(type(()))

# 练习

T = (
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa'],
)

print(T[0][0]) # 打印Apple
print(T[1][1]) # 打印Python
print(T[2][2]) # 打印Lisa
