class Solution():
	def readBinaryWatch(self, n):


#The code has O(1) time complexity, because all the possible watch combinations (valid or invalid) can’t be more that 12 * 59.
#Regarding space complexity, it’s also O(1) cause the DFS will have depth of maximum n, which can’t be more than 9 as per problem boundary.
        def dfs(n, hours, mins, idx):
        	if hours >= 12 or mins > 59: return
        	if not n:
        		res.append(str(hours) + ":" + "0" * (mins<10) + str(mins))
        		return
        	for i in range(idx, 10):
        		if i < 4:
        			dfs(n-1, hours | (1 << i), mins, i+1)
        		else:
        			k = i - 4
        			dfs(n-1, hours, mins| (1<< k), i+1)
        res = []
        dfs(n, 0, 0, 0)
        return res

## just loop over all possible combination, easy to write out
    def readBinaryWatch2(self, n):
    	output = []
    	for h in range(12):
    		for m in range(60):
    			if bin(h*64 + m).count('1') == n:
    				output.append('%d:%02d' % (h, m))
    	return output

    def readBinaryWatch3(self, n):
    	return ['%d:%02d' % (h, m)
    	for h in range(12) for m in range(60)
    	if (bin(h) + bin(m)).count('1') == n]
