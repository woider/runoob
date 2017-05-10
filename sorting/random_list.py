from random import random
from json import dumps, loads

from exec_time import exectime


# 生成随机数文件
@exectime
def dump_random_array(file, size):
    fo = open(file, 'w', 1024)
    numlst = list()
    for i in range(size):
        numlst.append(int(random() * 10 ** 10))
    fo.write(dumps(numlst))
    fo.close()


# 加载随机数列表
def load_random_array(file):
    fo = open(file, 'r', 1024)
    try:
        numlst = fo.read()
    finally:
        fo.close()
    return loads(numlst)


# print(dump_random_array('numbers.json', 10 ** 6))
