class Solution(object):
    def getMinimumDifference(self, root):
        def inorder(root, res):
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
        res = []
        inorder(root, res)
        return min([abs(a-b) for a, b in zip(res, res[1:])])

