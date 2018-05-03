

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
