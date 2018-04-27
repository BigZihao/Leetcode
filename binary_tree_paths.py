class Solution(object):
## dfs + stack
	def binaryTreePaths2(self, root):
		if not root:
			return []
		res, stack = [], [(root, "")]
		while stack:
			node, ls = stack.pop()
			if not node.left and not node.right:
				res.append(ls + str(node.val))
			if node.right:
				stack.append((node.right, ls+str(node.val)+"->"))
			if node.left:
				stack.append((node.left, ls+str(node.val)+"->"))
		return res

## dfs recursively
    
    def binaryTreePath3(self, root):
    	if not root:
    		return []
    	res = []
    	self.dfs(root, "", res)
    	return res

    def dfs(self, root, path, res):
    	if not root.left and not root.right:
    		res.append(path + str(root.val))
    	if root.left:
    		self.dfs(root.left, path+str(root.val) + "->", res)
    	if root.right:
    		self.dfs(root.right, path+str(root.val)+"->", res)
   


	def binaryTreePaths(self, root):
		if not root:
			return []
		return [str(root.val) + '->' + path
		for kid in (root.left, root.right) if kid
		for path in self.binaryTreePaths(kid)] or [str(root.val)]



