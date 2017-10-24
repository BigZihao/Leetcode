class Solution(object):
	def binaryTreePaths(self, root):
		if not root:
			return []
		return [str(root.val) + '->' + path
		for kid in (root.left, root.right) if kid
		for path in self.binaryTreePaths(kid)] or [str(root.val)]

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

