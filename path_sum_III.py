class Solution(object):
	def pathSum(self, root, target):
		def findSum(root, totSum):
			if not root: return 
			totSum+=root.val
			res[0]+=partSums[totSum - target]
			partSums[totSum]+=1
			findSum(root.left, totSum)
			findSum(root.right, totSum)
			partSums[totSum]-=1

		res = [0]
		partSums = collections.Counter([0])
		findSum(root, 0)
		return res[0]

	def pathSum2(self, root, s):
		return self.helper(root, s, [s])

	def helper(self, node, origin, targets):
		if not node: return 0
		hit = 0
		for t in targets:
			if not t-node.val: hit+=1
		targets = [t-node.val for t in targets]+[origin]
		return hit + self.helper(node.left, origin, targets) + self.helper(node.right, origin, targets)

    def pathSum3(self, root, target):
    	self.count = 0
    	preDict = {0:1}
    	def dfs(p, target, pathSum, preDict):
    		if p:
    			pathSum+=p.val
    			self.count+=preDict.get(pathSum - target, 0)
    			preDict[pathSum] = preDict.get(pathSum, 0)+1
    			dfs(p.left, target, pathSum, preDict)
    			dfs(p.right, target, pathSum, preDict)
    			preDict[pathSum]-=1
    	dfs(root, target, 0, preDict)
    	return self.count