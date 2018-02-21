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
    			stack.append()
    			x+=1
    	
