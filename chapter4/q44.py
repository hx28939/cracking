#from BinaryTreeNode import *


class ListNode:
	
	def __init__(self, val):
		self.val = val
		self.next = None


class LinkedList:
	
	def __init__(self):
		self.head = None
		self.tail = None
	
	def addNode(self, val):
		node = ListNode(val)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

def bfs(tree):
	result = []
	level = LinkedList()
	if tree is not None:
		level.addNode(tree)
	while level.head is not None:
		result.append(level)
		next_level = LinkedList()
		current = level.head
		while current is not None:
			if current.val.left is not None:
				next_level.addNode(current.val.left)
			if current.val.right is not None:
				next_level.addNode(current.val.right)
			current = current.next
		level = next_level
	return result
	
def dfs(tree, result = None, deep = 0):
	if result == None:
		result = []
	if tree is None:
		return result
	if deep == len(result):
		current = LinkedList()
		result.append(current)
	result[deep].addNode(tree)
	deep += 1
	dfs(tree.left, result, deep)
	dfs(tree.right, result, deep)
	return result


		
		

def printList(result):
	for i, j in enumerate(result):
		print i, "level:",
		p = j.head
		while p is not None:
			print p.val.val
			p = p.next
		print ""

class BinaryTreeNode:
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None
	def setLeft(self, l_val):
		leftnode = BinaryTreeNode(l_val)
		self.left = leftnode
		if leftnode != None:
			leftnode.parent = self
	def setRight(self, r_val):
		rightnode = BinaryTreeNode(r_val)
		self.right = rightnode
		if rightnode != None:
			rightnode.partent = self



tree = BinaryTreeNode(5)
tree.setLeft(3)
tree.left.setLeft(1)
tree.left.left.setRight(2)
tree.left.setRight(4)
tree.setRight(6)
tree.right.setRight(8)

print "D F S:"
printList(dfs(tree))
print "B F S:"
printList(bfs(tree))