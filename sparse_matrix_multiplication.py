class Solution(object):
	def multiply(self, A, B):
		mA, nA, nB = len(A), len(A[0]), len(B[0])
		res = [[0]*len(B[0]) for _ in range(mA)]
		for i in range(mA):
			for j in range(nA):
				## check Each Element of the Sparse matix A, if zero, don't even start the loop for B
				if A[i][j]:
					for k in range(nB):
						res[i][k]+ = A[i][j]*B[j][k]

		return res

# time m*n*nB
# space m*nB

