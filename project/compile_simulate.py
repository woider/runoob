
'''
算符优先分析过程模拟

设计一个给定算符优先分析表，输入一个句子，能由依据算符优先分析表输出与句子对应的语法树。
能对语法树生成过程进行模拟。
'''
import time

# 算符优先分析表
relation = {
    '+': {'+': '>', '-': '>', '*': '<', '/': '<', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '-': {'+': '>', '-': '>', '*': '<', '/': '<', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '*': {'+': '>', '-': '>', '*': '>', '/': '>', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '/': {'+': '>', '-': '>', '*': '>', '/': '>', '(': '<', ')': '>', 'i': '<', '#': '>'},
    '(': {'+': '<', '-': '<', '*': '<', '/': '<', '(': '<', ')': '=', 'i': '<', '#': ' '},
    ')': {'+': '>', '-': '>', '*': '>', '/': '>', '(': ' ', ')': '>', 'i': ' ', '#': '>'},
    'i': {'+': '>', '-': '>', '*': '>', '/': '>', '(': ' ', ')': '>', 'i': ' ', '#': '>'},
    '#': {'+': '<', '-': '<', '*': '<', '/': '<', '(': '<', ')': ' ', 'i': '<', '#': '='},
}


# 打印算符关系表
def print_relation_table(relation):
    separator = '{:-^%d}' % (len(relation['#']) * 10 + 11)
    print('\n' + separator.format(''))
    print('|' + '{:^9}'.format('') + '|', end='')
    for key in relation['#'].keys():
        print('{:^9}'.format(key), end='|')
    print('\n' + separator.format(''))
    for lkey in relation.keys():
        print('|' + '{:^9}'.format(lkey), end='|')
        for rkey in relation[lkey].keys():
            print('{:^9}'.format(relation[lkey][rkey]), end='|')
        print('\n' + separator.format(''))


# 算符优先规约过程
def analysis_process(expression):
    stack = ['#']
    process = []
    array = list(expression + '#')
    left, right, isMove = '', '', True
    while not (len(stack) == 1 and len(array) == 0):
        info = ['', '', '', '', '']
        # 取出符号
        left = ''.join(stack).replace('E', '')[-1]
        if len(array) and isMove:
            right = array.pop(0)
        # 组装参数
        info[0] = ''.join(stack)  # 栈
        info[1] = relation[left][right]  # 优先关系
        info[2] = right  # 当前符号
        info[3] = ''.join(array)  # 剩余输入串
        # 移进操作
        if info[1] == '<':
            isMove = True
            stack.append(right)
            info[4] = '移进'
        # 规约操作
        elif info[1] == '>':
            isMove = False
            if stack[-1] == 'E':
                info[4] = '规约 E->' + ''.join(stack[-3:])
                stack = stack[:-3]
                stack.append('E')
            if stack[-1] == 'i':
                info[4] = '规约 E->i'
                stack[-1] = 'E'
        elif info[1] == '=':
            isMove = True
            stack.append(right)
            if left == '#':
                info[4] = '接受'
            else:
                info[4] = '规约 E->' + ''.join(stack[-3:])
            stack = stack[:-3]
            stack.append('E')
        process.append(info)
    return process


# 打印规约过程
def print_process(process):
    form = '|{0:^9}|   {1:<13}|{2:^11}|{3:^11}|{4:>13}   |  {5:<13}|'
    print('{:-<87}'.format(''))
    for i in range(len(process)):
        print(form.format('(%d)' % (i + 1), *tuple(process[i])))
        print('{:-<87}'.format(''))
        time.sleep(1)  # 定时打印


# 程序执行
expression = input('输入表达式：').replace(' ', '')
process = analysis_process(expression)
print_process(process)
