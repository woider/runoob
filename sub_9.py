'''
题目：模拟Linux用户登录。验证账号和密码，若不匹配则暂停三秒输出错误信息。

程序分析：使用time模块的sleep()方法，可以让程序休眠一段时间。
'''

import time

global user,name
user = {
    'woider':'3243',
}

def login():
    global name
    name = input('Username:')
    pswd = input('Password:')
    if name not in user:
        return False
    return user[name] == pswd

while(not login()):
    time.sleep(3) # 暂停3秒
    print('Authentication failure')

print(name + '@localhost:~$')
