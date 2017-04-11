'''
单例模式
'''

class Singleton:
	__object = None
	def instance(self):
		pass

class Object:
	def __init__(self):
		pass

# 饿汉模式
class SingleHung(Singleton):
	__object = Object()

	def instance(self):
		return self.__object

# 懒汉模式
class SingleLazy(Singleton):
	__object = None

	def instance(self):
		if self.__object == None:
			self.__object = Object()
		return self.__object

hung = SingleHung()
hung1 = hung.instance()
hung2 = hung.instance()
print('hung1:0x%x | hung2:0x%x'%(id(hung1),id(hung2)))

lazy = SingleLazy()
lazy1 = lazy.instance()
lazy2 = lazy.instance()
print('lazy1:0x%x | lazy2:0x%x'%(id(lazy1),id(lazy2)))