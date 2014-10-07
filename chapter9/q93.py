
def magic(array, start, end):
	mid = (start + end) / 2
	if array[mid] == mid:
		return mid
	elif array[mid] > mid:
		return magic(array, start, mid)
	else:
		return magic(array, mid, end)


array = [-1,-1,-1,3,3,4,5,7,7,7,9,10,11,13]
print magic(array, 0, len(array) - 1)