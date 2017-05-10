'''
归并排序
'''

from exec_time import exectime

from random_list import load_random_array


@exectime
def merge_sort(array):
    # merge array
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

    # recursion
    def merge_rec(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = merge_rec(array[:mid])
        arr_r = merge_rec(array[mid:])
        return merge_arr(arr_l, arr_r)

    return merge_rec(array)


array = load_random_array('numbers.json')
print(merge_sort(array))
