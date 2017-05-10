'''
原生排序
'''
from exec_time import exectime
from random_list import load_random_array


@exectime
def python_sort(array):
    array.sort()
    return array


array = load_random_array('numbers.json')
print(python_sort(array))
