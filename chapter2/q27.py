class Node:
	def __init__(self, x):
		self.val = x
		self.next = None

def palindrome(head):
	if head == None:
		return
	slow = head
	fast = head
	stack = []
	while fast.next and fast.next.next:
		stack.append(slow.val)
		slow = slow.next
		fast = fast.next.next
	stack.append(slow.val)
	
	if fast.next:
		slow = slow.next
	
	while slow.next:
		if slow.val == stack.pop():
			slow = slow.next
		else:
			#print "FALSE"
			return False
	#print "TRUE"
	return True
	
a=Node('a')
b=Node('b')
c=Node('c')
d=Node('d')
e=Node('c')
f=Node('b')
g=Node('a')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

a1=Node('1')
b1=Node('2')
c1=Node('3')
d1=Node('3')
e1=Node('2')
f1=Node('1')

a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e1
e1.next = f1

print palindrome(a)
print palindrome(a1)