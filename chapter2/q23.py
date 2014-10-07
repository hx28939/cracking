class Node:
	def __init__(self, x):
		self.val = x
		self.next = None
	
def removeNode(c):
	if c == None or c.next == None:
		print 'FALSE'
		return False
	c.val = c.next.val
	c.next = c.next.next

a=Node('f')
b=Node('o')
c=Node('l')
d=Node('l')
e=Node('o')
f=Node('w')
g=Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

removeNode(c)
p = a
while p.next:
	print p.val
	p = p.next
print p.val