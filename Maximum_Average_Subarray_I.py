#Maximum_Average_Subarray_I


# In the first approach, we calculate P[i] = A[0] + A[1] + ... + A[i-1] in linear time. Then, A[i] + A[i+1] + ... + A[i+K-1] = P[i+K] - P[i], and we should find the max of these.
def finMaxAverage(self, A, K):
	P = [0]
	for x in A:
		P.append(P[-1] + x)

	ma = max(P[i+K] - P[i] for i in range(len(A) - K + 1))
	return ma/float(K)



# sliding window

def findMaxAverage(self, A, K):
	maxSum = curSum = sum(nums[:K])
	for i in range(len(nums) - K):
		curSum = curSum + nums[i+K] - nums[i]
		maxSum = max(maxSum, curSum)
	return maxSum/fload(K)
