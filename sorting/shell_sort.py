'''
希尔排序
'''
from exec_time import exectime

from random_list import load_random_array


@exectime
def shell_sort(array):
    gap = len(array)
    while gap > 1:
        gap = gap // 2
        for i in range(gap, len(array)):
            for j in range(i % gap, i, gap):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
    return array


array = load_random_array('numbers.json')
print(shell_sort(array))
