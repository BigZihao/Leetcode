# Time Complexity - O(V + E)， Space Complexity - O(V)
# 原文作者表示，想要提高速度到O(V+E)，必须把输入换成邻接表的形式。
class Solution(object):
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        # use DFS to parse the course structure
        self.graph = collections.defaultdict(list) # a graph for all courses
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        self.visited = [0 for x in xrange(numCourses)] # DAG detection 
        for x in xrange(numCourses):
            if not self.DFS(x):
                return []
             # continue to search the whole graph
        return self.res
    
    def DFS(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for x in self.graph[node]:
            if not self.DFS(x): ### recursive call to find the sink vertext or circle
                return False
        self.visited[node] = 1 # mark as finished
        self.res.append(node) # add to solution as the course depenedent on previous ones
        return True


    def findOrder2(self, numCourses, prerequisites):
    	dic = collections.defaultdict(set)
    	neigh = collections.defaultdict(set)
    	for i, j in prerequisites:
    		dic[i].add(j)
    		neigh[j].add(i)
    	stack = [i for i in range(numCourses) if not dic[i]]
    	res = []
    	while stack:
    		node = stack.pop()
    		res.append(node)
    		for i in neigh[node]:
    			dic[i].remove(node)
    			if not dic[i]:
    				stack.append(i)
    		dic.pop(node)
    	return res if not dic else []


    def findOrder2(self, numCourses, prerequisites):
        self.res = []
        in_degree = [0]*numCourses
        out_degree = [[] for _ in range(numCourses)]
        for p in prerequisites:
            in_degree[p[0]]+=1
            out_degree[p[1]].append(p[0])
        q = []
        k=0
        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)
        while q:
            x = q.pop()
            k+=1
            self.res.append(x)
            for i in out_degree[x]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    q.append(i)
        return self.res if k==numCourses else []