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

	def findTilt(self, root):
		if not root:
			return 0
		def csum(root):
			if not root:
				return 0
			return root.val + csum(root.left) + csum(root.right)
		return abs(csum(root.left) - csum(root.right)) + self.findTilt(root.left) + self.findTilt(root.right)

	

