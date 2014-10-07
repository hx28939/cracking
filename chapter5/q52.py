
def decimals(n):
	b = 0
	res = ''
	while n != 0 and b < 32:
		n = n * 2
		if n >= 1:
			res = res + '1'
			n -= 1
		else:
			res = res + '0'
		b += 1
	if b == 32 and n != 0:
		print "ERROR"
	else:
		res = '0.' + res
		print res

a = 0.6
decimals(a)
