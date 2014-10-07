class SingleStack:
	def __init__(self):
		self.stack = []
		self.min = []
	
	def push(self, val):
		self.stack.append(val)
		if len(self.min) == 0 or val < self.min[-1]:
			self.min.append(val)
	
	def pop(self):
		if len(self.stack) == 0:
			return "trying pop an empty array"
		val = self.stack.pop()
		if val == self.min[-1]:
			self.min.pop()
		return val
	
	def theMin(self):
		if len(self.min)== 0:
			return 
		return self.min[-1]
		
from random import randrange
stack = SingleStack()
for i in range(15):
	data = randrange(1,100)
	stack.push(data)
	print data
print ""
for i in range(15):
	print "poped", stack.pop(), "new min", stack.theMin()