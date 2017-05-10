'''
选择排序
'''
from exec_time import exectime

from random_list import load_random_array


@exectime
def select_sort(array):
    for i in range(len(array)):
        x = i  # min index
        for j in range(i, len(array)):
            if array[j] < array[x]:
                x = j
        array[i], array[x] = array[x], array[i]
    return array


array = load_random_array('numbers.json')
print(select_sort(array))



