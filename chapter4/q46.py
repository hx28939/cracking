
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

def findNextNode(root):
	if root == None:
		return None
	if root.right:
		return findMostLeft(root.right)
	else:
		return findNextParent(root)

def findMostLeft(root):
	if root.left == None:
		return root
	else:
		return findMostLeft(root.left)

def findNextParent(root):
	parent = root.parent
	current = root
	while parent != None and parent.left is not current:
		parent = parent.parent
		current = current.parent
	return parent
	
tree = TreeNode(5)
tree.setLeft(3)
tree.left.setLeft(1)
tree.left.setRight(4)
tree.setRight(7)
tree.right.setRight(9)

for node in [tree, tree.left.right, tree.right, tree.right.right]:
	next = findNextNode(node)
	print node.val, "next:", next.val if next else next