from collections import deque
from collections import defaultdict
from typing import List

class WeightedEdge:
    def __init__(self, var_name: str, weight: float):
        self.var_name = var_name
        self.weight = weight

class BFSResolver:
    def __init__(self):

        self.adj: defaultdict = defaultdict(list)

    def build(self, equations: List[List[str]], values: List[float]):
        if len(equations) != len(values):
            return

        for edge, weight in zip(equations, values):
            self.add_edge(edge[0], edge[1], weight)

    def bfs_find(self, query: List[str]) -> float:

        u, v = query

        q: deque = deque()

        if len(self.adj[v]) == 0:
            return -1.0
        if u == v:
            return 1.0
        q.append((1, v))

        visited: defaultdict = defaultdict(bool)
        visited[v] = True
        while q:
            val, node = q.popleft()

            for w_e in self.adj[node]:
                if not visited[w_e.var_name]:
                    new_val = val * w_e.weight

                    if w_e.var_name == u:
                        return new_val
                    q.append((new_val, w_e.var_name))
                    visited[w_e.var_name] = True

        return -1.0

    def add_edge(self, u: str, v: str, weight: float):
        self.adj[u].append(WeightedEdge(v, 1 / weight))
        self.adj[v].append(WeightedEdge(u, weight))


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        res: List[float] = []

        bfs_resolver = BFSResolver()
        bfs_resolver.build(equations, values)

        for query in queries:
            res.append(bfs_resolver.bfs_find(query))

        return res


sln = Solution()
e1 = [["a","b"],["b","c"]]
v1 = [2.0,3.0]
q1 = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

print(sln.calcEquation(e1, v1, q1))

e2 = [["a","b"],["b","c"],["bc","cd"]]
v2 = [1.5,2.5,5.0]
q2 = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]

print(sln.calcEquation(e2, v2, q2))

e3 = [["a","b"]]
v3 = [0.5]
q3 = [["a","b"],["b","a"],["a","c"],["x","y"]]

print(sln.calcEquation(e3, v3, q3))
