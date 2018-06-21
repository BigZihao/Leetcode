

1. minimum size subarray sum
def minSubArrayLen(self, s, nums):
	total = left = 0
	result = len(nums) + 1
	for right, n in enumerate(nums):
		total+=n
		while total >= s:
			result = min(result, right - left + 1)
			total-= nums[left]
			left+= 1
	return result if result <= len(nums) else 0



2. longest substring without repeating chractors

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    res = 0
    start = 0
    for i, string in enumerate(s):
        if string not in dic.keys() or dic[string] < start:
            res = max(res, i-start+1)
        else:
            start = dic[string] +1
        dic[string] = i
    return res