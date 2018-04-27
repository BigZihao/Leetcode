class Solution(object):
	def buildTree(self, preorder, inorder):
		if inorder:
			ind = inorder.index(preorder.pop(0))
			root = TreeNode(inorder[ind])
			root.left = self.buildTree(preorder, inorder[:ind])
			root.right = self.buildTree(preorder, inorder[ind+1:])
			return root