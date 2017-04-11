'''
代理模式
'''

# 图像接口 
class Image:
	def display(self):
		pass

# 图像对象
class RealImage(Image):
	__fileName = ''
	
	def __init__(self,fileName):
		self.__fileName = fileName
		self.__loadFromDisk(fileName)
	
	def display(self):
		print('Displaying ' + self.__fileName)

	def __loadFromDisk(self,fileName):
		print('Loading ' + fileName)

# 图像对象代理
class ProxyImage(Image):
	__image = None
	
	def __init__(self,fileName):
		self.__image = RealImage(fileName)
	
	def display(self):
		self.__image.display()


image = ProxyImage('C:/Users/Public/Pictures/Sample.jpg')

image.display()