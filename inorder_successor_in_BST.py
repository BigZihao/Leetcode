class Solution():
	def inorderSuccessor(self, root, p):
		succ = None
		while root:
			if p.val < root.val:
				succ = root
				root = root.left
			else:
				root = root.right
		return succ