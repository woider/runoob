'''
工厂模式
'''

# 运算类
class Operation:
	def oper(self,a,b):
		pass

# 加法类
class OperAdd(Operation):
	def oper(self,a,b):
		return a + b

# 减法类
class OperSub(Operation):
	def oper(self,a,b):
		return a - b

# 乘法类
class OperMul(Operation):
	def oper(self,a,b):
		return a * b

# 除法类
class OperDiv(Operation):
	def oper(self,a,b):
		return a / b

# 工厂类
class Factory:
	def select(self,opt):
		if opt == '+':
			return OperAdd()
		elif opt == '-':
			return OperSub()
		elif opt == '*':
			return OperMul()
		elif opt == '/':
			return OperDiv()

a = float(input('input a:'))
opt = str(input('input o:'))
b = float(input('input b:'))

res = Factory().select(opt).oper(a,b)
print(a,opt,b,'=',res)