
def next_step(step, remain, ways):
	remain -= step
	if remain == 0:
		ways += 1
		return ways
	if remain < 0:
		return ways
	ways += next_step(1, remain, ways) + next_step(2, remain, ways) + next_step(3, remain, ways)
	return ways
	
n = 4
print next_step(0, n, 0)
	