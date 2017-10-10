#Remove Duplicates from Sorted Array

# time O(nlogn)
def removeDuplicates(self, nums):
	"""
	type nums: List[int]
	rtype: int
	"""
	nums[:] = sorted(list(set(nums)))
	return len(nums)


# time O(n)
def removeDuplicates2(self, nums):
	"""
	type nums: List[int]
	rtype: int
	"""
    if not nums:
        return 0
    
    newtail = 0
    for num in nums:
        if num!=nums[newtail]:
            newtail+=1
            nums[newtail] = num
    return 1+newtail
    