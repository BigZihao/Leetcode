class Solution():
	## insert the new value, at any position in between of previous results
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
			for p in self.permuteII3(nums[:nums.index(n)] + nums[nums.index(n)+1:])] or [[]]


	def permuteII4(self, nums):
		if not nums:
			return []
		### sorted first jump over same value to avoid duplicate. 
		nums = sorted(nums)
		res = []
		path = []
		self.dfs(nums, path, res)
		return res

	def dfs(self, s, path, res):
		if not s:
			res.append(path)
			return

		for i in range(len(s)):
			if i>0 and s[i]==s[i-1]:
				continue
			self.dfs(s[:i] + s[i+1:], path + [s[i]], res)




        



from functools import reduce
if __name__ == "__main__":
	print(Solution().permuteII([1,2,2,3]))
	print(Solution().permuteII2([1,2,2,3]))
	print(Solution().permuteII3([1,2,2,3]))
	print(Solution().permuteII4([1,2,2,3]))
