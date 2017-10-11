

class Solution(object):
## DP recursion

	def maxSubArray(self, nums):
		n = len(nums)
		if n==1:
			return nums[0]
		return max(self.maxSubArray(nums[:n-1])+nums[-1], nums[-1])

## the problem seems to has to do with the topological order. the final result is actually depend on all previous i


	### O(n) time, O(1) space

	def maxSubArray2(self, nums):
		if not nums:
			return 0
		curSum = maxSum = nums[0]
		for num in nums[1:]:
			curSum = max(curSum + num, num)
			maxSum = max(maxSum, curSum)
		return maxSum



	def maxSubArray3(self, nums):
		for i in range(1, len(nums)):
			nums[i] = max(nums[i], nums[i] + nums[i-1])
		return max(nums)


	def maxSubArray4( elf, nums):
		for i in range(1, len(nums)):
			if nums[i-1]>0:
				nums[i]+=nums[i-1]
		return max(nums)




if __name__ == "__main__":
	print( Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) )
	print( Solution().maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]) )