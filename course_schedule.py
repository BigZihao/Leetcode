class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]

        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j):
                return False

        visited[i] = 1
        
        return True
## The topological sort is natural for this problem. We always take the courses with no unstudied prereqs and so on until no more courses we can take. The oud[i] is the number of prereqs for course i and indegree keep a list of courses require course i.
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_degree = [0]*numCourses
        out_degree = [[] for _ in range(numCourses)]
        for p in prerequisites:
            in_degree[p[0]]+=1
            out_degree[p[1]].append(p[0])
        q = []
        for i in range(numCourses):
            if in_degree[i]==0:
                q.append(i)
        k = 0
        while q:
            x = q.pop()
            k+=1
            for i in out_degree[x]:
                in_degree[i]-=1
                if in_degree[i] == 0:
                    q.append(i)
        return k == numCourses


## topological sort
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        stack = [n for n in range(numCourses) if not graph[n]]
        count = 0
        while stack:
            node = stack.pop()
            count+=1
            for n in neighbors[node]:
                graph[n].remove(node)
                if not graph[n]:
                    stack.append(n)
        return count == numCourses







1. if node v has not been visited, then mark it as 0.
2. if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
3. if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.