class Solution():

	#recursion
	def combine1(self, n, k):
		if k == 0:
			return [[]]
		return [pre + [i] for i in range(k, n+1) for pre in self.combine1(i-1, k-1)]

	def combine2(self, n, k):
		combs = [[]]
		for _ in range(k):
			combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
		return combs

### Combinations is typical application for backtracking. 
#Two conditions for back track: 
#(1) the stack length is already k 
#(2) the current value is too large for the rest slots to fit in since we are using ascending order to 
# make sure the uniqueness of each combination.
	def combine3(self, n, k):
		ans = []
		stack = []
		x = 1
		while True:
			l = len(stack)
			if l == k:
				ans.append(stack[:])
			if l == k or x> n-k+l+1:
				if not stack:
					return ans
				x = stack.pop() + 1
			else:
				stack.append(x)
				x+=1

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(xrange(1,n+1), k, 0, [], res)
        return res

    def dfs(self, nums, k, index, path, res):
        if k > len(nums) - index + 1: return  ## to save some time. or prune search path
        elif k == 0:
            res.append(path)
            return
        for i in xrange(index, len(nums)):
            self.dfs(nums, k-1, i+1, path+[nums[i]], res)


            

if __name__ == "__main__":
	print(Solution().combine1(5, 2))
	print(Solution().combine2(5, 2))
	print(Solution().combine3(5, 2))
	print(Solution().combine4(5, 2))
