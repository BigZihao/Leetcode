#Rotate_Function

def maxRotateFunction(self, A):
	"""
	type A: List[int]
	rtype: int
	"""
	# We should compute F[i+1] based on F[i]
	n = len(A)
	s = sum(A)
	F0 = sum(i*j for i, j in zip(range(n),A))
	max_F = F0
	F = F0
	for last_item in reversed(A[1:]):# last_item in B0, B1, ..
		F+= s - n*last_item
		max_F = max(max_F, F)
	return max_F

def maxRotateFunction(self, A):
	if len(A) == 0:
		return 0
	totalSum = sum(A)
	lMax = 0
	for i in range(len(A)):
		lMax+=i*A[i]
	gMax = lMax
	for i in range(len(A)-1, 0, -1):
		lMax += (totalSum - A[i]*len(A))
		gMax = max(gMax, lMax)
	return gMax