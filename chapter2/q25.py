class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

def add2num(a,b):
	if a == None and b == None:
		return
	elif a == None:
		return b
	elif b == None:
		return a
	else:
		result = Node(0)
		p = result
		t = 0
		while a and b:
			sum = a.val + b.val + t
			t = sum / 10
			v = sum % 10
			p.next = Node(v)
			p = p.next
			a = a.next
			b = b.next
		while a:
			sum = a.val + t
			t = sum / 10
			v = sum % 10
			p.next = Node(v)
			p = p.next
			a = a.next
		while b:
			sum = b.val + t
			t = sum / 10
			v = sum % 10
			p.next = Node(v)
			p = p.next
			b = b.next
	return result.next
	
a = Node(3)
a.next = Node(1)
a.next.next = Node(5)
b = Node(5)
b.next = Node(9)
b.next.next = Node(2)
d = None
c = add2num(a,b)
while c.next:
	print c.val
	c = c.next
print c.val