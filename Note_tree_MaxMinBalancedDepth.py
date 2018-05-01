Tree
about the depth
recursively


1. maximum depth of tree
2. mimium depth of tree
3. balanced binary tree

1. Maximum depth of Tree

def maxDepth(self, root):
    return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0

2. Minimum depth of tree

def minDepth(self, root):
    if root is None:
        return 0
    if root.left is None or root.right is None:
        return 1 + self.minDepth(root.left) + self.minDepth(root.right)
    return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # BFS   
def minDepth(self, root):
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if node:
            if not node.left and not node.right:
                return level
            else:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))


3. balanced tree

def isBalanced(self, root):
    def check(root):
        if root is None:
            return 0
        left = check(root.left)
        right = check(root.right)
        if left == -1 or right == -1 or abs(left - right)>1:
            return -1
        return 1+max(left, right)

    return check(root)!=-1


DFS
def isBalanced(self, root):
    stack, node, last, depths = [], root, None, {}
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1: return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True
