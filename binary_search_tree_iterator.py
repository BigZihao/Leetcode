class Solution(object):
	def __int__(self, root):
		self.stack = []
		while root:
			self.stack.append(root)
			root = root.left

	def hasNext(self):
		return len(self.stack)>0

	def next(self):
		node = self.stack.pop()
		x = node.right
		while x:
			self.stack.append(x)
			x = x.left
		return node.val