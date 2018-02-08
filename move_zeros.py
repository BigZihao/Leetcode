class Solution(object):
	# borrowed partition mechanism from quick sort
	def moveZeros(self, nums):
		zero = 0
		for i in range(len(nums)):
			if nums[i]!=0:
				nums[i], nums[zero] = nums[zero], nums[i]
				zero+=1
		return nums


if __name__ == "__main__":
	print(Solution().moveZeros([1,2,0,5,6,9,0,6,5]))
