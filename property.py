class Student(object):
	# sex = 'man' #类属性
	def __init__(self, name):
		super(Student, self).__init__()
		self.name = name #实例属性
s = Student('Tom')#动态的实例属性
s.score = 90
print('student:%s,score:%d'%(s.name,s.score))
s1 = Student('Tbby')
# print('student:%s,sex:%s'%(s1.name,s1.sex))

# class Person(object):
# 	__slots__ = ('name','age')# 用tuple定义允许绑定的属性名称

# p = Person()
# p.name = 'May'
# p.age = '8'
# print('person:%s,age:%s',%(p.name,p.age))
# p.score = '100'


		