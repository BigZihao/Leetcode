class Solutions(object):
	def diameterOfBinaryTree(self, root):
		self.best = 0
		def depth(root):
			if not root: return 0
			ansL = depth(root.left)
			ansR = depth(root.right)
			self.best = max(self.best, ansL + ansR )
			return 1 + max(ansL, ansR)
		depth(root)
		return self.best 