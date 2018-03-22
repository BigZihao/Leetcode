class Solution(object):
	## recursive version
#If both trees are empty then we return empty.
#Otherwise, we will return a tree. The root value will be t1.val + t2.val, except these values are 0 if the tree is empty.
#The left child will be the merge of t1.left and t2.left, except these trees are empty if the parent is empty.
#The right child is similar.
	def mergeTrees(self, t1, t2):
		if t1 and t2:
			root = TreeNode(t1.val + t2.val)
			root.left = self.mergeTrees(t1.left, t2.left)
			root.right = self.mergeTrees(t1.right, t2.right)
			return root
		else:
			return t1 or t2

	