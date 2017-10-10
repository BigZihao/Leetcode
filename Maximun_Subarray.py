


### O(n) time, O(1) space

def maxSubArray(self, nums):
	if not nums:
		return 0
	curSum = maxSum = nums[0]
	for num in nums[1:]:
		curSum = max(curSum + num, num)
		maxSum = max(maxSum, curSum)
	return maxSum



def maxSubArray(self, nums):
	for i in range(1, len(nums)):
		nums[i] = max(nums[i], nums[i] + nums[i-1])
	return max(nums)


def maxSubArray( elf, nums):
	for i in range(1, len(nums)):
		if nums[i-1]>0:
			nums[i]+=nums[i-1]
	return max(nums)