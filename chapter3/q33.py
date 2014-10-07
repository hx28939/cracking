class SetOfStacks:
	def __init__(self, capacity):
		self.capacity = capacity
		self.stack = []
	
	def push(self, val):
		if len(self.stack) == 0 or len(self.stack[-1]) == self.capacity:
			self.stack.append([])
		self.stack[-1].append(val)
	
	def pop(self):
		if len(self.stack) == 0:
			return "trying to pop an empty stack"
		data = self.stack[-1].pop()
		if len(self.stack[-1]) == 0:
			self.stack.pop()
		return data
			
	
	def popAt(self, index):
		if index < 1 or self.stack[index-1] == None:
			return "empty stack"
		data = self.stack[index-1].pop()
		if len(self.stack[index-1]) == 0:
			del self.stack[index-1]

			
test = SetOfStacks(8)
for i in range(24):
	test.push(i)
			

