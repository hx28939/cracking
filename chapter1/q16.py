

def transpose(matrix,n):
	for i in range(n-1):
		for j in range(i+1,n):
			matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

	#for i in range(n/2):
	#	for j in range(n):
	#		matrix[i][j],matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
	matrix.reverse()
	return matrix

a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print a[0]
print a[1]
print a[2]
print a[3]

b = transpose(a,4)
print b[0]
print b[1]
print b[2]
print b[3]




