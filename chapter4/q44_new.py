
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
		if self.head == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node

class TreeNode:
	
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None
	
	def setLeft(self, l_val):
		leftnode = TreeNode(l_val)
		self.left = leftnode
		if leftnode:
			leftnode.parent = self
	
	def setRight(self, r_val):
		rightnode = TreeNode(r_val)
		self.right = rightnode
		if rightnode:
			rightnode.parent = self

def bfs(root):
	result = []
	parent = LinkedList()
	parent.addnode(root)
	while parent.head:
		result.append(parent)
		children = LinkedList()
		current = parent.head
		while current:
			if current.left:
				children.addNode(current.left)
			if current.right:
				children.addNode(current.right)
			current = current.next
		parent = children
	return result

def dfs(root, result = None, deep = 0):
	if result == None:
		result = []
	if root == None:
		return result
	if deep == len(result):
		l = LinkedList()
		result.append(l)
	result[deep].addNode(root)
	deep += 1
	dfs(root.left, result, deep)
	dfs(root.right, result, deep)
	return result
	
def printList(result):
	for i, j in enumerate(result):
		print i, "level:",
		p = j.head
		while p:
			print p.val.val
			p = p.next
		print ""

tree = TreeNode(5)
tree.setLeft(3)
tree.left.setLeft(1)
tree.left.left.setRight(2)
tree.setRight(4)
tree.right.setLeft(6)
tree.right.setRight(8)

print "B F S"
printList(dfs(tree))
print "D F S"
printList(dfs(tree))