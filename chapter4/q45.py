
class TreeNode:
	
	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None
	
	def setLeft(self, L_val):
		leftnode = TreeNode(L_val)
		self.left = leftnode
		if leftnode:
			leftnode.parent = self
	
	def setRight(self, R_val):
		rightnode = TreeNode(R_val)
		self.right = rightnode
		if rightnode:
			rightnode.parent =self


def BST_check(root):
	if root == None:
		return True
		print "wan jie"
	if root.left and root.left.val > root.val:
		return False
	if root.right and root.right.val < root.val:
		return False
	if not BST_check(root.left) or not BST_check(root.right):
		return False
	return True

tree = TreeNode(4)
tree.setLeft(2)
tree.left.setLeft(1)
tree.left.setRight(3)
tree.setRight(6)
tree.right.setLeft(5)
print "Is the tree a binary search tree?"
print BST_check(tree)