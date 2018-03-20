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