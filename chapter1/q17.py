
def setRC0(matrix, m, n):
	row = [False] * m
	col = [False] * n
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				row[i] = True
				col[j] = True
	
	for i in range(m):
		for j in range(n):
			if row[i] or col[j]:
				matrix[i][j] = 0
	return matrix
	
a = [[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
setRC0(a,4,4)
print a[0]
print a[1]
print a[2]
print a[3]