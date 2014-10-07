
def get_n(l, i):
	list = []
	for j in range(l):
		b = i % 2
		i = i / 2
		list.append(b)
	return list
	
def subsets(set):
	l = len(set)
	result = []
	for i in range(pow(2, l)):
		list = get_n(l, i)
		sub_s = []
		for j in range(l):
			if list[j] == 1:
				sub_s.append(set[j])
		result.append(sub_s)
	return result
		

set = [1, 2,5]
print subsets(set)