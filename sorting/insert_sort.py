'''
插入排序
'''
from exec_time import exectime

from random_list import load_random_array


@exectime
def insert_sort(array):
    for i in range(len(array)):
        for j in range(i):
            if array[i] < array[j]:
                array.insert(j, array.pop(i))
                break
    return array


array = load_random_array('numbers.json')
print(insert_sort(array))
