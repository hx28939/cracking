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
			

class Solution:
	result = []
	def dfs(self, root, sum, valuelist):
		if sum == root.val:
			return Solution.result.append(valuelist)
		if root.left:
			self.dfs(root.left, sum - root.val, valuelist + [root.left.val])
		if root.right:
			self.dfs(root.right, sum - root.val, valuelist + [root.right.val])
	
	
	def pathsum(self, root, sum):
		if root == None:
			return []
		self.dfs(root, sum, [root.val])
		if root.left:
			self.pathsum(root.left, sum)
		if root.right:
			self.pathsum(root.right, sum)
		return Solution.result


givenSum = 7
root = TreeNode(1)
root.setLeft(2)
root.setRight(3)
root.left.setLeft(4)
root.left.setRight(5)
root.right.setLeft(3)
root.right.setRight(4)
root.left.right.setLeft(7)
	
solution = Solution()
solution.pathsum(root, givenSum)
for i in range(len(solution.result)):
	print solution.result[i]
    	
	
