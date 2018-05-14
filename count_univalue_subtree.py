class Solution():
	def countUnivalueSubtree(self, root):
		self.count = 0
		self.checkUni(root)
		return self.count

	def checkUni(self, root):
		if not root:
			return True
		l, r = self.checkUni(root.left), self.checkUni(root.right)
		if l and r and (not root.left or root.left.val == root.val) and (not root.right or root.right.val == root.val):
			self.count+=1
			return True
		return False
