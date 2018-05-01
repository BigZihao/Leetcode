class Solution(object):

## width has a relation with levels/depth

	def widthOfBinaryTree(self, root):
		if not root:
			return 0
		q = [[root, 0]]
		res = 0
		while q:
			size = len(q)
			level = []
			for _ in range(size):
				n, pos = q.pop(0)
				level.append(pos)
				if node.left: q.append([n.left, pos*2])
				if node.left: q.append([n.right, pos*2+1])
			res = max(res, level[-1] - level[0] + 1)
		return res


	def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = [[root,0]]
        res = 0
        while q:
            newq = []
            alllabel = []
            while q:
                node, label = q.pop(0)
                alllabel.append(label)
                if node.left:
                    newq.append([node.left,2*label])
                if node.right:
                    newq.append([node.right, 2*label+1])
            res =max(res, alllabel[-1] - alllabel[0] +1)
            q = newq
        return res
                    