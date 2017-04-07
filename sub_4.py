'''
题目：输入某年某月某日，判断这一天是这一年的第几天？

程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
'''

cal = input('日期：')

date = cal.split('-')

year = int(date[0])
month = int(date[1])
day = int(date[2])

# print(year,month,day)

arr = [0,31,28,31,30,31,30,31,31,30,31,30,31]

num = 0

if ((year%4==0) and (year%100!=0)) or (year%400==0):
    arr[2] = 29

for i in range(1,len(arr)):
    if month > i:
        num += arr[i]
    else:
        num += day
        break

print('天数：',num)
