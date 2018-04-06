class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        visited = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[x] = graph.get(x, []) + [y]
        
        self.res = []
        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return []
        return self.res
    ## the only change here is to detech circle

    def dfs(self, graph, visited, i):
        if visited[i]==-1:
            return False
        if visited[i]==1:
            return True
        visited[i]=-1
        for j in graph.get(i,[]):
            if not self.dfs(graph, visited, j):
                return False
        
        visited[i]=1  ## once it add into visited, says it is the last node in the graph
        self.res.append(i) 
        return True
        

        # DFS


    def findOrder(self, numCourses, prerequisites):
        dic = collections.defaultdict(set)
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack = [i for i in xrange(numCourses) if not dic[i]]  ## those have no child is the last node
        res = []
        while stack:
            node = stack.pop()
            res.append(node) # the last node can be add to res directly
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []


  # BFS
    def findOrder1(self, numCourses, prerequisites):
        dic = {i: set() for i in xrange(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []
    