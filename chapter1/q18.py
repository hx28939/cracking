
def isSubstring(s1,s2):
	return (s2 in s1)

def isRotation(s1, s2):
	if len(s2)>len(s1):
		return False
	else:
		return isSubstring(s1+s1,s2)

s1 = "apple"
s2 = "pleap"
print isRotation(s1,s2)