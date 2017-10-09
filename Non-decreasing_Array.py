# Non-decreasing Array



def checkPossibility(self, nums):
	count_dec=0
	for i in range(len(nums)-1):
		if nums[i]>nums[i+1]:
			count_dec+=1
			if i==0:
				nums[i]=nums[i+1]
			elif nums[i-1]<=nums[i+1]:
				nums[i] = nums[i-1]
			else:
				nums[i+1]=nums[i]
		if count_dec>1:
			return False
	reutn True




def checkPossibility(self, nums):
	count = 0
	for i in range(len(nums)-1):
		if nums[i]>nums[i+1]:
			count+=1
			if count>1 or ((i-1>=0 and nums[i-1]>nums[i+1]) and (i+2<len(nums) and nums[i]>nums[i+2])):
				return False
	return True





def checkPossibility(self, nums):
	one, two = nums[:], nums[:]
	for i in range(len(nums)-1):
		if nums[i]>nums[i+1]:
			one[i] = nums[i+1]
			two[i+1] = nums[i]
		break
	return one == sorted(one) or two == sorted(two)