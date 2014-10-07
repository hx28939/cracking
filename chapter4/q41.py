
class TreeNode(object):
	
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.parent = None
	
	def setLeftChild(self, leftnode):
		self.left = leftnode
		if leftnode != None:
			leftnode.parent = self
	
	def setRightChild(self, rightnode):
		self.right = rightnode
		if rightnode != None:
			rightnode.parent = self
	
def isBalanced(root):
	if root == None:
		return True
	heightDiff = getHeight(root.left) - getHeight(root.right)
	if abs(heightDiff) > 1:
		return False
	return isBalanced(root.left) and isBalanced(root.right)

def getHeight(root):
	if root == None:
		return 0
	else:
		return max(getHeight(root.left), getHeight(root.right)) + 1
		
tree = TreeNode(1)
tree.setLeftChild(TreeNode(2))
tree.setRightChild(TreeNode(3))
tree.left.setLeftChild(TreeNode(4))
tree.left.left.setLeftChild(TreeNode(5))

print isBalanced(tree)