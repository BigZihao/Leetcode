# p(r,w) = 0, when w = 0. Waral 博客有更多文章,
# p(r,w) = 1, when r = 0, w > 0
# p(r,w) = w/(r+w)*p(r,w-1) + r/(r+w)*[w/(r+w)*p(r,w-1) + r/(r+w)*p(r-1,w)], otherwise


# dp[i][j] = 1.0 * i / (i + j) * dp[i-1][j]. 留学申请论坛-一亩三分地
# + 1.0 * j / (i + j) * (1.0*i/(i+j)*dp[i-1][j] + 1.0*j/(i+j)*dp[i][j-1]);. 
# pro is the probability of last one is white with initial i white and j red

# dynamic programming

##
# Randomly select a bean from the jar and if it is white, eat it.
# Otherwise return the bean to the jar, randomly select a bean again and eat it regardless of color.


class Solution():
	def bean(w, r): 
## red col, white row
	    dp = [[0]*r]*w
	    if w == 0 and r == 0:
	    	return 0
	    if r == 0:
	    	return 1
	    if w == 0:
	    	return 0

	    dp[0][0] = 0
	    dp[0][1] = 0
	    dp[1][0] = 1

	    for i in range(1, w):
	    	for j in range(1, r):
	    		dp[i][j] = i/(i+j)*dp[i-1][j] + j/(i+j)*(i/(i+j)*dp[i-1][j] + j/(i+j)*dp[i][j-1])
	    return dp[-1][-1]

if __name__ == '__main__':
	p  = Solution.bean(4,4)
	print(p)
