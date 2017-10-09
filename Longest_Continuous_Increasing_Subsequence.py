# Longest_Continuous_Increasing_Subsequence

def findLengthofLCIS(self, nums):
	max_len = i =0
	N = lens(nums)
	while i < N:
		curr = 1
		while nums[i]<numsp[i+1] and i+1<N:
			curr, i = curr+1, i + 1
		max_len = max(max_len, curr)
		i+=1
	return max_len




def findLenthofLCIS(self, nums):
	if len(nums) == 0:
		return 0
	max_len = 1
	prev = nums[0]
	curr_len = 1
	for i in range(1, len(nums)):
		if nums[i] > prev:
			curr_len+=1
		else:
			curr_len = 1
		max_len = max(max_len, curr_len)
		prev = nums[i]
	return max(curr_len, max_len)