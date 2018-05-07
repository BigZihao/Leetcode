class Solution(object):
	def productExceptSelf(self, nums):
		p = 1
		n = len(nums)
		output = []
		for i in range(n):
			output.append(p)
			p = p*nums[i]

		# now output has all the left product results
		p = 1
		for i in range(n-1, -1, -1):
			output[i] = output[i]*p
			p = p*nums[i]
		# not output has all the right product results

		return output

