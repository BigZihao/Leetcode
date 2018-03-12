class Solutions(object):
	#O(1) space think of two pointers
    # Use two-pointers: two pointers start from back
    # first pointer j stop at descending point
    # second pointer i stop at value > nums[j]
    # swap and sort rest
	def nextPermutation(self, nums):
		if not nums: return None
		i = len(nums) - 1
		j = -1
		while i > 0:
			if nums[i-1] < nums[i]:
				j = i - 1
				break
			i-=1
		for i in range(len(nums)-1, -1, -1):
			if nums[i] > nums[j]:
				nums[i], nums[j]  = nums[j], nums[i]
				nums[j+1:] = sorted(nums[j+1:])
				return
