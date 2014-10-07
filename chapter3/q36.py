
class Stack:

	def __init__(self):
		self.stack = []
	
	def push(self, val):
		self.stack.append(val)
	
	def pop(self):
		if self.isEmpty():
			return "EMPTY"
		return self.stack.pop()
	
	def peek(self):
		if self.isEmpty():
			return "EMPTY"
		return self.stack[-1]
	
	def isEmpty(self):
		return len(self.stack) == 0
		
def sortStacks(s):
	new_s = Stack()
	while not s.isEmpty():
		data = s.pop()
		while not new_s.isEmpty() and new_s.peek() > data:
			s.push(new_s.pop())
		new_s.push(data)
	return new_s

from random import randrange
stack = Stack()
for i in range(10):
	stack.push(randrange(0,100))
print "before", stack.stack
print "after", sortStacks(stack).stack
