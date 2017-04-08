'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。

程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''

arr_str = input('请输入三个整数：\n')

arr = arr_str.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort(reverse=False)

print('排序结果：\n' + str(arr))
