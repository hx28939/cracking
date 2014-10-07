
class TreeNode:

	def __init__(self, val):
		self.val = val
		self.parent = None
		self.left = None
		self.right = None
	
	def setLeftChild(self, leftval):
		leftnode = TreeNode(leftval)
		self.left = leftnode
		if leftnode != None:
			leftnode.parent = self
	
	def setRightChild(self, rightval):
		rightnode = TreeNode(rightval)
		self.right = rightnode
		if rightnode != None:
			rightnode.parent = self


def printTree(tree):
	if tree != None:
		print tree.val
		print tree.val, "left:",
		printTree(tree.left)
		print tree.val, "right:",
		printTree(tree.right)

def create_tree(array, start, end):
	if start > end:
		return None
	mid = (start + end) >> 1
	tree = TreeNode(array[mid])
	tree.left = create_tree(array, start, mid - 1)
	tree.right = create_tree(array, mid + 1, end)
	return tree

array = [1, 2, 3, 4, 5, 6, 7]
tree = create_tree(array, 0, len(array) - 1)
printTree(tree)