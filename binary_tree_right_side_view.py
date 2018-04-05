class Solutions(object):
    def rightSideView(self, root):
        res, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(curr.val)
                stack.append((curr.right, level+1))
                stack.append((curr.left, level + 1))
        return [x[-1] for  x in res]

    def rightSideView2(self, root):
        def collect(node, depth):
            if node:
                # DFS-traverse the tree right-to-left, add values to the view whenever we first reach a new record depth. This is O(n).
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)
        view = []
        collect(root, 0)
        return view

    def rightSideView3(self, root):
        if not root:
            return []
        q = [root]
        res = []
        while q:
            new_q = []
            for node in q:
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            res.append(node.val)
            q = new_q
        return res

