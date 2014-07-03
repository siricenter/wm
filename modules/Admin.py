# custom classes

class AdminStuff(object):
	z = 2
	def __init__(self,a,b):
		self.x = a
		self.y = b
	def add(self):
		return self.x + self.y + self.z
		