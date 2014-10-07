
class SingleArrayStacks(object):
	def __init__(self, stacksize = 100, number = 3):
		self.stacksize = stacksize
		self.number = number
		self.array = [None] * self.stacksize * self.number
		self.pointer = [-1] * self.number
	
	def push(self, stacknum, value):
		if self.pointer[stacknum] + 1 >= self.stacksize:
			print "out of space"
		else:
			self.pointer[stacknum] += 1
			self.array[self.stacktop(stacknum)] = value
	
	def pop(self, stacknum):
		if self.pointer[stacknum] < 0:
			return "trying to pop an empty stack."
		else:
			data = self.array[self.stacktop(stacknum)]
			self.array[self.stacktop(stacknum)] = None
			self.pointer[stacknum] -= 1
			return data
	
	def peek(self, stacknum):
		if self.pointer[stacknum] < 0:
			print "empty stack"
		else:
			return self.array[self.stacktop(stacknum)]
	
	def isEmpty(self, stacknum):
		return self.pointer[stacknum] == -1
			
	def stacktop(self, stacknum):
		return self.stacksize * stacknum + self.pointer[stacknum]
		
array = SingleArrayStacks()
array.push(2,11)