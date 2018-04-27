class Solution(object):
	def __init__(self):
		self.prev = None

	def flatten(self, root):
		if not root:
			return 
		self.prev = root
		self.flatten(root.left)

		temp = root.right
		root.right, root.left = root.left, None
		self.prev.right = temp

		self.flatten(temp)