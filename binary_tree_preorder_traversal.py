class Solution(object):
	def preorderTraversal(self, root):
		res = []
		stack = [root]
		while stack:
			node = stack.pop()
			if node:
				res.append(node.val)
				stack.append(node.right)
				stack.append(node.left)
		return res
		# recursively
	def preorderTraversal1(self, root):
	    res = []
	    self.dfs(root, res)
	    return res
	    
	def dfs(self, root, res):
	    if root:
	        res.append(root.val)
	        self.dfs(root.left, res)
	        self.dfs(root.right, res)