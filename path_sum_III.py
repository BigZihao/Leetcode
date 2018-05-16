class Solution(object):

# Two Sum Method: Optimized Solution

# A more efficient implementation uses the Two Sum idea. 
It uses a hash table (extra memory of order N). With more space, 
it gives us an O(N) complexity.
# As we traverse down the tree, at an arbitrary node N, we store the sum until this node N (sum_so_far (prefix) + N.val). in hash-table. Note this sum is the sum from root to N.
# Now at a grand-child of N, say G, we can compute the sum from the root until G since we have the prefix_sum until this grandchild available.We pass in our recursive routine.
# How do we know if we have a path of target sum which ends at this grand-child G? Say there are multiple such paths that end at G and say they start at A, B, C where A,B,C are predecessors of G. Then sum(root->G) - sum(root->A) = target. Similarly sum(root->G)-sum(root>B) = target. Therefore we can compute the complement at G as sum_so_far+G.val-target and look up the hash-table for the number of paths which had this sum
# Now after we are done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended at a predecessor node.

class Solution(object):
    def helper(self, root, target, so_far, cache):
        if root:
            complement = so_far + root.val - target
            if complement in cache:
                self.result += cache[complement]
            cache.setdefault(so_far+root.val, 0)
            cache[so_far+root.val] += 1
            self.helper(root.left, target, so_far+root.val, cache)
            self.helper(root.right, target, so_far+root.val, cache)
            cache[so_far+root.val] -= 1
        return

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.result = 0
        self.helper(root, sum, 0, {0:1})
        return self.result




# Brute Force Solution

# The simplest solution is to traverse each node (preorder traversal) and 
# then find all paths which sum to the target using this node as root.
# The worst case complexity for this method is N^2.
# If we have a balanced tree, we have the recurrence: T(N) = N + 2T(N/2). This is the merge sort recurrence and suggests NlgN.

class SolutionBruteForce(object):
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + self.find_paths(root.left, target-root.val) + 
            self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.find_paths(root, sum) + 
            self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0








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

<<<<<<< HEAD




=======
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
>>>>>>> 451fd64b8af546b9c06c436e81da0a472ec36498
