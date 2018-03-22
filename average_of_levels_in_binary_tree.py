class solutions(object):
	def averageOfLevels(self, root):
		info = []
		def dfs(node, depth = 0):
			if node:
				if len(info) <= depth:
					info.append([0, 0])
				info[depth][0]+=node.val
				info[depth][1]+=1
				dfs(node.left, depth+1)
				dfs(node.right, depth+1)
	dfs(root)
	return [s/float(c) for s, c in info]
## BFS
## Time:  O(n)
## Space: O(h)
    def averageOfLevels(self, root):
    	result = []
    	q = collections.deque([root])
    	while q:
    		total, count = 0, 0 
    		next_q = collections.deque([])
    		while q:
    			n = q.popleft()
    			total+=n.val
    			count+=1
    			if n.left:
    				next_q.append(n.left)
    			if n.right:
    				next_q.append(n.right)
    		q, next_q = next_q, q
    		result.append(float(total) / count)
    	return result

## short BFS
	def averageOfLevels2(self, root):
		ans = []
		lvl = [root]
		while lvl:
			ans.appen(sum(n.val for n in lvl) / float(len(lvl)))
			lvl = [c for n in lvl for c in [n.left, n.right] if c]
		return ans