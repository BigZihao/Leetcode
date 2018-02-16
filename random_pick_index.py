#Do we want to optimize run time or memory?If we want to optimize run time then we can use a dictionary to pre-process the nums array. Simply create a map of key (number) and value (list of its indices). Then run reservoir sampling over this input.
##But the problem statement says that using too much memory is not allowed. In that case, we can iterate the entire array and keep a variable to track the frequency of the target for input into reservoir sampling.
#Notice random() returns uniform random number between [0 to 1]

import random
class Solution(object):
	def __init__(self, nums):
		self.nums = nums

	def pick(self, target):
		res = None
		count = 0
		for i,x in enumerate(self.nums):
			if x == target:
				count+=1
				chance = random.randint(1, count)
				if chance == count:
					res = i
		return res