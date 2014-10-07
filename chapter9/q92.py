
def possibleWays(x, y):
	if x == 1 or y == 1:
		return 1
	return possibleWays(x-1, y) + possibleWays(x, y-1)

def path(x, y, un_array):
	total = possibleWays(x,y)
	un = 0
	for i in un_array:
		un += possibleWays(i[0], i[1]) * possibleWays(x - i[0] + 1, y - i[1] + 1)
	return total - un	
	
	
	
x = 4
y = 4
un_array = [[2,2]]
print path(x, y, un_array)
