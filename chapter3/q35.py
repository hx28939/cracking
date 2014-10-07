class MyQueue:

	def __init__(self):
		self.queue1 = Stack()
		self.queue2 = Stack()
	
	def push(self, val):
		self.queue1.push(val)
	
	def pop(self):
		if len(self.queue2.stack) == 0 and len(self.queue1.stack) == 0:
			return "EMPTY"
		elif len(self.queue2.stack) == 0:
			while len(self.queue1.stack) != 0:
				self.queue2.push(self.queue1.pop())
		return self.queue2.pop()
	
	def peek(self):
		if len(self.queue1.stack) == 0 and len(self.queue2.stack) == 0:
			return "EMPTY"
		elif len(self.queue1.stack) == 0:
			while len(self.queue2.stack) != 0:
				self.queue1.push(self.queue2.pop())
		return self.queue1.pop()
			
class Stack:
	
	def __init__(self):
		self.stack = []
	
	def push(self, val):
		self.stack.append(val)
	
	def pop(self):
		if len(self.stack) == 0:
			return
		else:
			return self.stack.pop()
	
	def peek(self):
		if len(self.stack) == 0:
			return
		else:
			return self.stack[-1]

queue = MyQueue()
for i in range(1,5):
	queue.push(i)
	print "Enqueued", i
	queue.push(i*2)
	print "enqueued", i*2
data = queue.pop()
print "dequeued", data
			