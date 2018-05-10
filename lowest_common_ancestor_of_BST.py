class Solution(object):
	## iteration
	def lowestCommonAncestor(self, root, p, q):
		while root:
			if root.val > p.val and root.val > q.val:
				root = root.left
			elif root.val < p.val and root.val < q.val:
				root = root.right
			else:
				return root

	def lowestCommonAncestor(self, root, p, q):
		while (root.val-p.val)*(root.val - q.val)>0:
			if root.val>max(p.val, q.val):
				root = root.left
			else:
				root = root.right
		return root


	## recursion
	def lowestCommonAncestor2(self, root, p, q):
		if (p.val <= root.val <= q.val or q.val <= root.val <= p.val): return root
		if (p.val < root.val and q.val < root.val): return self.lowestCommonAncestor2(root.left, p, q)
		if (p.val > root.val and q.val > root.val): return self.lowestCommonAncestor2(root.right, p, q)