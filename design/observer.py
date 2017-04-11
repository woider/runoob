'''
观察者模式
'''
# 观察者接口
class Observer:
	def update(self):
		pass

# 观察对象接口
class Subject:
	def regObs(self,obs):
		pass
	def remObs(self,obs):
		pass
	def notObs(self):
		pass

# 学校（观察者）
class School(Subject):
	__list = list()
	def regObs(self,obs):
		self.__list.append(obs)

	def remObs(self,obs):
		self.__list.remove(obs)

	def notObs(self):
		for item in self.__list:
			item.update()

# 学生（观察对象）
class Student(Observer):
	__name = ''
	def __init__(self,name):
		self.__name = name
	def update(self):
		print('学生'+self.__name+'回教室')

# 老师（观察对象）
class Teacher(Observer):
	__name = ''
	def __init__(self,name):
		self.__name = name
	def update(self):
		print(self.__name[0]+'老师开始上课')


school = School()

student1 = Student('小明')
student2 = Student('小红')

teacher1 = Teacher('李湘之')
teacher2 = Teacher('张全蛋')

# 观察对象注册
school.regObs(student1)
school.regObs(student2)
school.regObs(teacher1)
school.regObs(teacher2)

# 观察对象移除 
school.remObs(teacher2)

school.notObs()




