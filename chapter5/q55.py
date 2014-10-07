
def get1s(n):

	one = 0
	while n > 0:
		b = n % 2
		one += b
		n = n / 2
	return one
	
	
def No_bits(a, b):
	xor = a ^ b
	return get1s(xor)
	

print No_bits(31,14)  #output: 2 
