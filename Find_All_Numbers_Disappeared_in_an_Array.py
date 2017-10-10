#Find All Numbers Disappeared in an Array


## the idea is similar to keep an index, but to avoid extra space, it use the negative to indicate the index
def findDisappearedNumber(self, nums):
	n = len(nums)
	for i in range(n):
		index = abs(nums[i]) - 1
		nums[index] = -abs(nums[index])  # abs it to avoid occur twice
	return [i + 1 for i in range(n) if nums[i]>0]