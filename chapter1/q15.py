
def q15(s):
	length = len(s)
	pre = s[0]
	count = 1
	res = ''
	for i in range(1,length):
		if s[i] == pre:
			count += 1
		else:
			res = res + pre + str(count)
			count = 1
			pre = s[i]
	res = res + pre +str(count)
	if len(res) >= length:
		return s
	else:
		return res
			
test_1 = 'aabbbbbccddd'
test_2 = 'abcde'

print q15(test_1)
print q15(test_2)