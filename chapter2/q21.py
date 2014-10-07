
class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

		
def removedulicate(head):
	if head == None:
		return
	#result = Node(0)
	#result.next = head
	cur = head
	nn = head.next
	ku = [head.val]
	
	while nn:
		
		if nn.val in ku:
			cur.next = nn.next
			nn = cur.next
			
		else:
			ku.append(nn.val)
			cur = nn
			nn = nn.next
	
	return head

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

p = a
while p.next:
	print p.val
	p = p.next
print p.val
removedulicate(a)

p = a
while p.next:
	print p.val
	p = p.next

print p.val
