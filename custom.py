 class Student(object):
 	def __init__(self, name):
		self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name