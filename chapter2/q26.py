class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

def loopstart(head):
	list = []
	while head:
		if head in list:
			return head
		else:
			list.append(head)
			head = head.next
	return head

a=Node('f')
b=Node('o')
c=Node('a')
d=Node('l')
e=Node('p')
f=Node('w')
g=Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = c

result = loopstart(a)
print result.val