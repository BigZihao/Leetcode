class Solution(object):
	def longestUnivaluePath(self, root):
		longest = [0]
		def traverse(node):
			if not node:
				return 0
			left_len, right_len = traverse(node.left), traverse(node.right)
			left = (left_len + 1) if node.left and node.left.val == node.val else 0
			right = (right_len + 1) if node.right and node.right.val == node.val else 0
			longest[0] = max(longest[0], left + right)
			return max(left, right)
		traverse(root)
		return longest[0]


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
