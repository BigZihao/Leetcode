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


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        self.dfs(root, sum, [], res)
        return res
    
    def dfs(self, root, sum, path, res):
        if root and root.left and root.right :
            self.dfs(root.left, sum-root.val, path + [root.val], res) or self.dfs(root.right, sum-root.val, path + [root.val], res)
        elif root.left:
            self.dfs(root.left, sum-root.val, path + [root.val], res)
        elif root.right:
            self.dfs(root.right, sum - root.val, path + [root.val], res)
        else:
            if sum == root.val:
                res.append(path + [root.val])
                return