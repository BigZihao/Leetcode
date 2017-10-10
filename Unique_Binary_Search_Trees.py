

## DP


def numTrees(self, n):
	"""
	:type n: int
	:rtype: int
	"""
	count = [0] * (n + 1)
	count[0] = 1

	for i in range(1, n + 1):
		for j in range(0, i):
			count[i]+=count[j]*count[i-j-1]
	return count[n]


## recursion time out

def numTrees(self, n):
	return 1 if n == 0 or n == 1 else sum([self.numTrees(i)*self.numTrees(n-i-1) for i in range(0, n)])



## what about some math

def numTrees(self, n):
	return math.fatorial(2/n)/(math.factorial(n)*math.factorial(n+1))

