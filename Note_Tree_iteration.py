
1. inorder interation
2. BST iterator
3. binary tree traversal
space complexity: O(h) where h is the height of the tree
best/average O(log(n))
worst case O(n)

time complexity: O(n)

inorder of BST is the sorted order 

1. inorder iteration
def inorderTraversal1(self, root):
    res = []
    self.helper(root, res)
    return res

def helper(self, root, res):
    if root:
        self.helper(root.left, res)
        res.append(root.val)
        self.helper(root.right, res)

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



2. BST iterator
def __init__(self, root):
    """
    :type root: TreeNode
    """
    self.stack = []
    while root:
        self.stack.append(root)
        root = root.left

def hasNext(self):
    return len(self.stack)>0

def next(self):
    node = self.stack.pop()
    x = node.right if node is not None else None
    while x:
        self.stack.append(x)
        x = x.left
    return node.val




3. binary tree traversal
3.1 breadth-first traversal:
level order
3.2 depth-first traversal:
preorder
inorder
postorder



 write the function recursively

4 max depth of tree
4.1 top down


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root, d):
            if root:
                self.res = max(self.res, d)
                depth(root.left, d+1)
                depth(root.right, d+1)
        self.res = 0
        depth(root, 1)
        return self.res


4.2 bottom up
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if root:
                left = depth(root.left)
                right = depth(root.right)
                return max(left, right) + 1
            else:
                return 0
        res = depth(root)
        return res


5. symmetric tree

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def sym(L, R):
            if not L and not R:
                return True
            elif L and R and L.val == R.val:
                return sym(L.left, R.right) and sym(L.right, R.left)
            else:
                return False
        return sym(root, root)