
array = [0, 1, 2, 3, 4, 5, 7]
sum = 0
l = len(array)
for i in array:
	sum += i
print l * (l + 1) / 2 - sum