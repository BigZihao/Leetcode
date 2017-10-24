class Solution(object):
	def trimBST(self, root, L, R):
		if not root:
			return None
		if root.val < L:
			return self.trimBST(root.right, L, R)
		elif root.val > R:
			return self.trimBST(root.left, L, R)
		root.left = self.trimBST(root.left, L, R)
		root.right = self.trimBST(root.right, L, R)
		return root

	def trimBST2(self, root, L, R):
		if root:
			root.left = self.trimBST2(root.left, L, R)
			root.right = self.trimBST2(root.right, L, R)
			return root.right if root.val<L else root.left if root.val>R else root