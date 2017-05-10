'''
冒泡排序
'''
from exec_time import exectime

from random_list import load_random_array


@exectime
def bubble_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array


array = load_random_array('numbers.json')
print(bubble_sort(array))
