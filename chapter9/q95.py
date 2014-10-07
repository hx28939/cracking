
def permutations(s, list):
	if len(list) == 0:
		list.append(s[-1])
	else:
		for i in range(len(list)):
			for j in range(len(list[i])):
				list.append(list[i][:j] + s[-1] + list[i][j:])
			list[i] += s[-1]
	print len(s)
	if len(s) == 1:
		return list
	else:
		return permutations(s[0:-1], list)
		

	
	
	
s = "abc"
print permutations(s, [])
