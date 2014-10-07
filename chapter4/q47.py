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
	
def father(root, node):
	if root == None:
		return False
	elif root == node:
		return True
	else:
		return father(root.left, node) or father(root.right, node)
		
	
def ancestor(root, node1, node2, result = None):
	if result == None:
		result = [None]
	if root and father(root, node1) and father(root, node2):
		result[0] = root
		#print root.val
		#print result.val
		ancestor(root.left, node1, node2, result)
		ancestor(root.right, node1, node2, result)
	return result[0]
	
def ancestor2(node1, node2):
	while node1:
		p2 = node2
		while p2:
			if node1 == p2:
				return node1
			p2 = p2.parent
		node1 = node1.parent
	return None

	

root = TreeNode(10)
root.setLeft(5)
root.setRight(6)
root.left.setLeft(1)
root.left.setRight(2)
root.right.setLeft(3)
root.right.setRight(4)
root.left.right.setLeft(7)

ans = ancestor(root, root.left.right.left, root.right)
ans2 = ancestor(root, root.left.right.left, root.left.right)
ans3 = ancestor(root, root.right, TreeNode(0))

an = ancestor2(root.left.right.left, root.right)
an2 = ancestor2(root.left.right.left, root.left.right)
an3 = ancestor2(root.right, TreeNode(0))

#print ans.val if ans else ans
#print ans2.val if ans2 else ans2
#print ans3.val if ans3 else ans3

print an.val if an else an
print an2.val if an2 else an2
print an3.val if an3 else an3