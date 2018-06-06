# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """        if not root: return []
        if not root.left and not root.right: return [root.val]

        leaves = []
        def traverse(root):
            if not root.left and not root.right:
                leaves.append(root)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(root)

        left = []
        node = root
        while node and node != leaves[0]:
            left.append(node)
            if node.left: node = node.left
            else: node = node.right

        right = []
        node = root
        while node and node != leaves[-1]:
            right.append(node)
            if node.right: node = node.right
            else: node = node.left

        left = left[1:] if root.left else []
        right = right[1:] if root.right else []
        return [node.val for node in [root] + left + leaves + right[::-1]]