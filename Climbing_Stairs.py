
def climbstairs(self, n):
	if n == 1:
		return 1
	if n == 2:
		return 2
	return self.climbstairs(n - 1) + self.climbstairs(n - 2)



## bottom up, O(n) space
def climbstairs(self, n):
	if n == 1:
		return 1
	res = [0 for i in range(n)]
	res[0], res[1] = 1, 2
	for i in range(2, n):
		res[i] = res[i-2] + res[i-1]
	return res[-1]