from collections import deque

class Animal(object):
	def __init__(self, name):
		self.name = name
		self.order = -1
	def __str__(self):
		return "animal:" + self.name

class Dog(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)
	def __str__(self):
		return "dog:" + self.name

class Cat(Animal):
	def __init__(self, name):
		Animal.__init__(self, name)
	def __str__(self):
		return "cat:" + self.name


class AnimalQueue(object):

	def __init__(self):
		self.dogs = deque()
		self.cats = deque()
		self.order = 0
		
	def enqueue(self, animal):
		animal.order = self.order
		self.order += 1
		if isinstance(animal, Dog):
			self.dogs.append(animal)
		else:
			self.cats.append(animal)
	
	def dequeueAny(self):
		if len(self.dogs) == 0:
			return self.dequeueCat()
		if len(self.cats) == 0:
			return self.dequeueDog()
		if self.dogs[0].order < self.cats[0].order:
			return self.dequeueDog()
		else:
			return self.dequeueCat()
	
	def dequeueDog(self):
		if len(self.dogs) == 0:
			return "NO DOG"
		else:
			return self.dogs.popleft()
	
	def dequeueCat(self):
		if len(self.cats) == 0:
			return "NO CAT"
		else:
			return self.cats.popleft()

animals = AnimalQueue()
animals.enqueue(Dog("dog1"))
animals.enqueue(Dog("dog2"))
animals.enqueue(Cat("cat1"))
animals.enqueue(Cat("cat2"))
animals.enqueue(Dog("dog3"))
animals.enqueue(Dog("dog4"))
print animals.dogs[1]
print animals.dequeueAny()
print animals.dequeueDog()
print animals.dequeueCat()

for i in range(3):
	print animals.dequeueAny()
print animals.dequeueAny()

