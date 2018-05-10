class solution():
	def rob(self, root):
		def dfs(root):
			if not root:
				return 0, 0 
			left, right = dfs(root.left), dfs(root.right)
			return (root.val + left[1] + right[1]), (max(left) + max(right))
		return max(dfs(root))