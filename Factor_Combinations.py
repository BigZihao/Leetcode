class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        nums = [i for i in range(2, n//2+1)]
        self.dfs(nums, 0, float(n), [], res)
        if res == [[]]:
            res = []
        return res
    
    def dfs(self, nums, index, target, path, res):
        if target == 1.0:
            res.append(path)
        if target < 1 or int(target)!=target:
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, i, float(target/nums[i]), path + [nums[i]], res)

## iterative backtracking

def getFactors(self, n):
	ans, stack, x = [], [], 2
	while True:
		if x > n/x:
			if not stack:
				return ans
			ans.append(stack + [n])
			x = stack.pop()
			n*=x
			x+=1
		elif n%x == 0:
			stack.append(x)
			n/=x
		else:
			x+=1


Iterative:

def getFactors(self, n):
    todo, combis = [(n, 2, [])], []
    while todo:
        n, i, combi = todo.pop()
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n/i],
                todo += (n/i, i, combi+[i]),
            i += 1
    return combis
Recursive:

def getFactors(self, n):
    def factor(n, i, combi, combis):
        while i * i <= n:
            if n % i == 0:
                combis += combi + [i, n/i],
                factor(n/i, i, combi+[i], combis)
            i += 1
        return combis
    return factor(n, 2, [], [])