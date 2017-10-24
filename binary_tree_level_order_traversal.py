class Solution(object):
	def levelOrder(self, root):
		ans, level = [], [root]
		while root and level:
			ans.append([node.val for node in level])
			LRpair = [(node.left, node.right) for node in level]
			level = [leaf for LR in LRpair for leaf in LR if leaf]
		return ans

	def levelOrder2(self, root):
		if not root:
			return []
		ans, level = [], [root]
		while level:
			ans.append([node.val for node in level])
			temp = []
			for node in level:
				temp.extend([node.left, node.right])
			level = [leat for leaf in temp if leaf]
		return ans

	def levelOrder3(self, root):
		if not root: return []
		stack, queue, res, nCount = [root], [], [[root.val]], 1
		while stack:
			temp = stack.pop(0)
			if temp.left:
				stack.append(temp.left)
			if temp.right:
				stack.append(temp.right)
			nCount-=1
			if nCount==0:
				queue = [x.val for x in stack]
				res+=[queue] if queue else []
				nCount = len(stack)
		return res

	def levelOrder4(self, root):
		if root is None: return []
		q = [[root]]
		for level in q:
			record = []
			for node in level:
				if node.left: record.append(node.left)
				if node.right: record.append(node.right)
			if record: q.append(record)
		return [[x.val for x  in level] for level in q]