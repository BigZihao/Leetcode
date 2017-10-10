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