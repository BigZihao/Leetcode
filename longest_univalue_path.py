class Solution(object):
	def longestUnivaluePath(self, root):
		self.longest = 0
		def traverse(node, parent_val):
			if not node:
				return 0
			left, right = traverse(node.left, node.val) , traverse(node.right, node.val)
			self.longest = max(self.longest, left + right)
			return 1 + max(left, right) if node.val == parent_val else 0
		traverse(root, None)
		return self.longest

	def longestUnivaluePath2(self, root):
		def dfs(root, res):
			l, r = 0, 0
			if root.left:
				l = dfs(root.left, res)
				l = l+1 if root.left.val == root.val else 0
			if root.right:
				r = dfs(root.right, res)
				r = r+1 if root.right.val == root.val else 0
			res[0] = max(res[0], r+1)
			return max(1, r)

		if not root:
			return 0
		res = [0]
		dfs(root, res)
		return res[0]
