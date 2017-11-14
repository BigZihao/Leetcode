# Third_Maximum_Number

def thirdMax(self, nums):
	l = [float('-inf')]*3
	for n in nums:
		if n > l[0] and n not in l:
			heapq.heappushpop(l, n)
	return l[0] if l[0]!=float('-inf') else max(l)