class Node:
	def __init__(self,x):
		self.val = x
		self.next = None

def findNthElement(head, n):
	if head == None:
		return
	p = head
	q = head
	while n>0 and q.next:
		q = q.next
		n -= 1
	
	while q:
		q = q.next
		p = p.next
	
	return p

a=Node('f')
b=Node('o')
c=Node('l')
d=Node('a')
e=Node('b')
f=Node('w')
g=Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

result = findNthElement(a,5)
print result.val