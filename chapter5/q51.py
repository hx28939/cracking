
def mergeMN(n, m, i, j):
	tail = n & ( (1 << i) - 1)
	head = (n >> (j + 1)) << (j + 1)
	result = head | (m << i) | tail
	return result

def print_b(n):
	res = ''
	while n >= 1:
		b = n % 2
		n = n / 2
		res = str(b) + res
	print res
	
n = 1<<10
m = 19
result = mergeMN(n,m,2,6)
print_b(result)