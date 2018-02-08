class Solution(object):
	def sortedArrayToBST(self, num):
		if len(num)==0:
			return None
		mid = len(num)//2
		node = TreeNode(num[mid])
		node.left = self.sortedArrayToBST(num[:mid])
		node.right = self.sortedArrayToBST(num[mid+1:])
		return node
