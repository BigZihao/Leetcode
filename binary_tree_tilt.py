class Solution(object):

	## postorder, left, right, root
	def findTilt(self, root):
		self.ans = 0
		def _sum(node):
			if not node: return 0
			left, right = _sum(node.left), _sum(node.right)
			## self.ans is keeping adding the tilt of each node
			self.ans+=abs(left - right)
			return node.val + left + right
			## but what we return is the 
		_sum(root)
		return self.ans

