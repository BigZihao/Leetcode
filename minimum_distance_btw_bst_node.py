class Solution(object):
	def minDiffInBST(self, root):
		min_diff = float('inf')
		in_list = self.inorder(root, [])
		for i in range(1, len(in_list)):
			min_diff = min(min_diff, in_list[i] - in_list[i-1])
		return min_diff

	def inorder(self, root, in_list):
		if root is None:
			return in_list
		self.inorder(root.left, in_list)
		in_list.append(root.val)
		self.inorder(root.right, in_list)
		return in_list