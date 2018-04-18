class Solution(object):
    def inorderTraversal1(self, root):
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)


    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        res = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            res.append(node.val)
            x = node.right
            while x:
                stack.append(x)
                x = x.left
        return res

    ## iteratively
    def inorderTraversal2(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res

    def inorderTraversal(self, root):
        result, stack = [], [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    result.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return result

### its basically the same as the binary search tree traversal 
### inorder traversal of BST will give us element in sorted order