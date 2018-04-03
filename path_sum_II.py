class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        stack = [(root, sum,[root.val])]
        res = []
        while stack:
            node, _sum, path = stack.pop()
            if node.left is node.right is None and node.val == _sum:
                res.append(path + [node.val])
            if node.left:
                stack.append((node.left, _sum - node.val, path+[node.val]))
            if node.right:
                stack.append((node.right, _sum - node.val,path+[node.val]))
        return res