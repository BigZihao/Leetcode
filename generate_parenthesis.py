class Solution(object):
	def generateParenthesis(self, n):
		if not n:
			return []
		left, right, ans = n, n, []
		self.dfs(left, right, ans, "")
		return ans

	def dfs(self, left, right, ans, string):
		if right < left:
			return 
		if not left and not right:
			ans.append(string)
			return
		if left:
			self.dfs(left - 1, right, ans, string + "(")
		if right:
			self.dfs(left, right - 1, ans, string + ")")



## To generate all n-pair parentheses, we can do the following:

#Generate one pair: ()

#Generate 0 pair inside, n - 1 afterward: () (…)…

#Generate 1 pair inside, n - 2 afterward: (()) (…)…

#…

#Generate n - 1 pair inside, 0 afterward: ((…))

#I bet you see the overlapping subproblems here. Here is the code:

#(you could see in the code that x represents one j-pair solution and y represents one (i - j - 1) pair solution, and we are taking into account all possible of combinations of them)

    def generateParenthesis2(self, n):
    	"""
    	:type n: int
    	:rtype: List[str]
    	"""
    	dp = [[] for i in range(n+1)]
    	dp[0].append('')
    	for i in range(n+1):
    		for j in range(i):
    			dp[i]+=['(' + x + ')' + y for x in dp[j] for y in dp[i-j-1]]
    	return dp[n]

    def generateParenthesis3(self, n, open = 0):
    	if n == 0: return [')'*open]
        if open == 0:
        	return ['('+x for x in self.generateParenthesis3(n-1, 1)]
        else:
        	return [')' + x for x in self.generateParenthesis3(n, open - 1)] + ['(' + x for x in self.generateParenthesis3(n-1, open + 1)]



if __name__=="__main__":
	print(Solution().generateParenthesis(3))