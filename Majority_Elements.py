def majorityElement1(self, nums):
	dic = {}
	for num in nums:
		dic[num] = dic.get(num, 0) + 1
	for num in nums:
		if dic[num] > len(nums)//2:
			return num 



def majorityElement2(self, nums):
	return sorted(nums)[len(nums)//2]


# the idea here is if a pair of elements from the
# list is not the same, then delete both, the last 
# remaining element is the majority number


def majorityElement3(self, nums):
	candidate = None
	count = 0
	for num in nums:
		if count == 0:
			candidate = num
			count+=1
		elif candidate == num:
			count+=1
		else:
			count-=1
	return candidate
