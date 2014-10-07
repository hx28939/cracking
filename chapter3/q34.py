class Hanoi:

	def __init__(self, size):
		self.towers = [[], [], []]
		self.size = size
		self.towers[0] = [x for x in range(size, 0, -1)]
		
	def moveDisk(self, size, fr, helper, to):
		if size == 1:
			data = self.towers[fr].pop()
			self.towers[to].append(data)
			print "disk", data, ": tower", fr, "->", to
		else:
			self.moveDisk(size - 1, fr, to, helper)
			self.moveDisk(1, fr, helper, to)
			self.moveDisk(size - 1, helper, fr, to)
	
	def printTowers(self):
		for i in self.towers:
			print i
	
	def playHanoi(self):
		self.printTowers()
		self.moveDisk(self.size, 0, 1, 2)
		self.printTowers()
		
test = Hanoi(1)
test.playHanoi()
		