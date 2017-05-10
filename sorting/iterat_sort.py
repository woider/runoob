from exec_time import exectime

from random_list import load_random_array


def merge_arr(arr_l, arr_r):
    array = []
    while len(arr_l) and len(arr_r):
        if arr_l[0] <= arr_r[0]:
            array.append(arr_l.pop(0))
        elif arr_l[0] > arr_r[0]:
            array.append(arr_r.pop(0))
    if len(arr_l) != 0:
        array += arr_l
    elif len(arr_r) != 0:
        array += arr_r
    return array


@exectime
def iterat_sort(array):
    array = list(map(lambda n: [n], array))
    while len(array) != 1:
        pool = []
        for i in range(0, len(array), 2):
            if (i + 1) < len(array):
                pool.append(merge_arr(array[i], array[i + 1]))
            else:
                pool.append(array[i])
        array = pool
    return array.pop()


array = load_random_array('numbers.json')
print(iterat_sort(array))
