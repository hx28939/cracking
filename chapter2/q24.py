class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

def partition(head, x):
	L_start = None
	L_end = None
	U_start = None
	U_end = None
	
	if head == None:
		return
	p = Node(0)
	p.next = head
	while p.next:
		if p.next.val < x:
			if L_start == None:
				L_start = Node(p.next.val)
				L_end = L_start
			else:
				L_end.next = Node(p.next.val)
				L_end = L_end.next
		else:
			#print p.val
			if U_start == None:
				U_start = Node(p.next.val)
				U_end = U_start
			else:
				U_end.next = Node(p.next.val)
				U_end = U_end.next
		p = p.next
	
	if L_start == None:
		return U_start
	else:
		L_end.next = U_start
		return L_start
	
a = Node(3)
a.next = Node(1)
a.next.next = Node(5)
a.next.next.next = Node(2)


c = partition(a,4)
while c.next:
	print c.val
	c = c.next
print c.val