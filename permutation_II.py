class Solution():
	def permuteII(self, nums):
		ans = [[]]
		for n in nums:
			new_ans = []
			for l in ans:
				for i in range(len(l)+1):
					new_ans.append(l[:i]+[n]+l[i:])
					if i < len(l) and l[i]==n:break
			ans = new_ans
		return ans

	def permuteII2(self, nums):
		perms = [[]]
		for n in nums:
			perms = [p[:i] + [n] + p[i:]
			for p in perms
			for i in range((p+[n]).index(n) + 1)]
		return perms

	def permuteII3(self, nums):
        return [[n] + p
            for n in set(nums)
            for p in self.permute(nums[:nums.index(n)] + nums[nums.index(n)+1:])] or [[]]
