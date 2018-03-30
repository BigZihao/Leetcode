class Solution(object):
    def calEquation(self, equations, values, queries):
 ## time O(V+E)
 ## space O(n)

#A series of equations A / B = k can be seen as a graph in which nodes are the dividend and divisor A and B and weights are the result of the division. So we simply create the graph and traverse it with DFS/BFS to get our result.

#Complexity is K * O(N + M) where N and M are the number of nodes and edges, and K is the number of queries. How many nodes can we have? It’s 2 * E, where E is the number of equations (2 different nodes per each equation). We can have at most E edges in the graph.

#So total complexity is O(K * E), with O(E) additional space for the graph.


        def dfs(start, end, path, paths):
            if start == end and start in G:
                paths[0] = path
                return
            if start in vis:
                return
            vis.add(start)
            for node in G[start]:
                dfs(node, end, path*W[start, node], paths)

        G, W = collections.defaultdict(set), collections.defaultdict(float)

        for (A, B), V in zip(equations, values):
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0/V

        res = []
        for X, Y in queries:
            paths, vis  = [-1.0], set()
            dfs(X, Y, 1.0, paths)
            res+=paths[0],
        return res

    def calcEquation(self, equations, values, queries):
        quot = collections.defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        for k, i, j in itertools.permutations(quot, 3):
            if k in quot[i] and j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
        return [quot[num].get(den, -1.0) for num, den in queries]