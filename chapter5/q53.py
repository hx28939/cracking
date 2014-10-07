
def larger(n):

	one = 0
	count = 0
	isFirstOne = True
	isFirstZero = True
	while isFirstZero or isFirstOne:
		b = n % 2
		one += b
		n = n / 2
		count += 1
		if isFirstZero and b == 1:
			isFirstOne = False
		if isFirstOne == False and b == 0:
			isFirstZero = False
			n = n<< 1
		if n == 0 and isFirstZero == True:
			isFirstZero = False
			n = 1
	n += 1
	n = n << (count - 1)
	n += max((1 << (one -1)) - 1, 0)
	return n


def smaller(n):
	
	one = 0
	count = 0
	isFirstOne = True
	isFirstZero = True
	while isFirstZero or isFirstOne:
		b = n % 2
		one += b
		n = n / 2
		count += 1
		if isFirstOne and b == 0:
			isFirstZero = False
		if isFirstZero == False and b == 1:
			isFirstOne = False
		if isFirstOne == True and n == 0:
			isFirstOne = False
			count -= 1
				
	n = n << count
	n += ((1 << (one)) -1) << (count - one - 1)
	return n
	
	
n = 8
print larger(n)
print smaller(n)