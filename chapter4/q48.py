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
			

def contain(T1, T2):
	if T2 == None:
		return True
	else:
		return search(T1, T2)
		
def search(T1, T2):
	if T1 == None:
		return False
	elif T1.val == T2.val:
		if match(T1, T2):
			return True
	else:
		return (search(T1.left, T2) or search(T1.right, T2))
		
			
def match(T1, T2):
	if T1 == None and T2 == None:
		return True
	elif T1 == None or T2 == None:
		return False
	elif T1.val != T2.val:
		return False
	else:
		return match(T1.left, T2.left) and match(T1.right, T2.right)

def test():
    T1 = TreeNode(1)
    T1.setLeft(2)
    T1.setRight(3)
    T1.left.setLeft(4)
    T1.left.setRight(2)
    T1.right.setRight(2)
    T1.left.right.setLeft(8)
    T2 = TreeNode(2)
    T2.setLeft(4)
    T2.setRight(2)
    T2.right.setLeft(8)
    
    #print contain(T1, None)          
    #print contain(None, T2)         
    #print contain(T1, T2)          
    print contain(T1, TreeNode(3))	
    
    
test()