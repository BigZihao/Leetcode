# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    ## dfs recursively
    def levelOrderBottom1(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)

    ## dfs+stack
    def levelOrderBottom2(self, root):
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

    ## bfs+queue
    def levelOrderBottom3(self, root):
        queue, res = collections.deque([root, 0]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res


    def levelOrderBottom4(self, root):
        answ, L = [], [root]
        while L and root:
            answ.insert(0, [n.val for n in L])
            L = [C for N in L for C in (N.left, N.right) if C]
        return answ
    
    def levelOrderBottom5(self, root):
        res, data = [], []
        if not root: return res
        stack = []
        stack.append(root)
        nCount = 1  ## record # of node at each level
        while stack:
            node = stack.pop(0)
            data+=[node.val]
            nCount-=1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if nCount == 0:
                res = [data] + res
                data = []
                nCount = len(stack)
        return res

    def levelOrderBottom6(self, root):
        if not root:
            return []
        from collections import deque
        result = deque()
        queue = deque([root])
        while(queue):
            level = []
            for i in range(len(queue)):
                front = queue.popleft()
                level.append(front.val)
                if front.left:
                    queue.append(front.left)
                if front.right:
                    queue.append(front.right)
            result.appendleft(level)
        return list(result)

    def levelOrderBottom7(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        result, current = [], [root]
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)

        return result[::-1]


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Solution().levelOrderBottom7(root)
    print (result)

