search

the comparison and transder between bfs dfs


从搜索树结构上讲，这类问题所有解的构造方式呈现 BFS 的分层结构，可以手动建立分层处理的机制处理。
与之相对的，最常见的递归解法是从 DFS 的角度去探索状态空间。

Iterative problem:
word ladder, 


1. from recursively dfs to iteratively bfs
1.1 binary tree path

# dfs + stack
def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res
    


# bfs + queue
def binaryTreePaths2(self, root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.left:
            queue.append((node.left, ls+str(node.val)+"->"))
        if node.right:
            queue.append((node.right, ls+str(node.val)+"->"))
    return res
    
# dfs recursively
def binaryTreePaths(self, root):
    if not root:
        return []
    res = []
    self.dfs(root, "", res)
    return res

def dfs(self, root, ls, res):
    if not root.left and not root.right:
        res.append(ls+str(root.val))
    if root.left:
        self.dfs(root.left, ls+str(root.val)+"->", res)
    if root.right:
        self.dfs(root.right, ls+str(root.val)+"->", res)



1.2 Phone Letter Combination
把这题单独拿出来，是因为这是个非常典型的递归 / 迭代都很直观的搜索类问题，一个 DFS，一个 BFS.




2. word ladder
著名 gay 题，时间复杂度爆炸的典范，
也是目前我知道的 leetcode 题里唯一一道非常适合使用 bi-directional bfs 的问题。
比较独特的是这题不是 DFS + Backtracking，主要原因在于我们要确保 “路线最短” ，
这个更适合用 BFS 解决，两层字典首次相交的地方一定是最短路线。