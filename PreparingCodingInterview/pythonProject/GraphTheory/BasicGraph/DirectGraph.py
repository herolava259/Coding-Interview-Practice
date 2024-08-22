from typing import List


class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v


class Graph:
    def __init__(self, g: List[List[int]], n: int, m: int):
        self.adj = g
        self.edges: List[Edge] = []
        self.num_node = n
        self.num_edge = m

        for u in range(1, self.num_node + 1):
            for v in self.adj[u]:
                if u < v:
                    self.edges.append(Edge(u, v))


class DirectGraphSolution:

    def __init__(self, g: List[List[int]], n: int, m: int):
        self.g = g
        self.num_nodes = n
        self.num_edges = m
        self.nums = [100_000_007 for _ in range(self.num_nodes + 1)]
        self.lowers = [100_000_007 for _ in range(self.num_nodes + 1)]
        self.time = 0
        self.bridge_flag = [False for _ in range(self.num_nodes + 1)]
        self.visited = [False for _ in range(self.num_nodes + 1)]
        self.dir_g: List[List[int]] = [[] for _ in range(self.num_nodes + 1)]
        self.bridges: List[Edge] = []

    def reset(self):
        for i in range(self.num_nodes + 1):
            self.nums[i] = 100_000_007
            self.lowers[i] = 100_000_007
        self.time = 0

    def dfs_solve(self, u: int, p: int):
        self.visited[u] = True
        self.time += 1
        self.nums[u] = self.time
        self.lowers[u] = self.time
        for v in range(self.num_nodes + 1):
            if v == p:
                continue
            if self.visited[v]:
                self.lowers[u] = min(self.lowers[u], self.nums[v])
                self.dir_g[u].append(v)
                continue
            self.dfs_solve(v, u)
            self.lowers[u] = min(self.lowers[u], self.lowers[v])
            self.dir_g[u].append(v)
            if self.lowers[v] > self.nums[u]:
                self.bridges.append(Edge(u, v))

    def dfs_get_strong_components(self, u: int, p: int, g: List[List[int]], visited: List[int]):

        self.visited[u] = True

        for v in g[u]:
            if v == p:
                continue
            if visited[v]:
                g[u].append(v)
                continue
            g[u].append(v)
            self.dfs_get_strong_components(v, u, g, visited)

    def get_all_strong_connected_components(self) -> List[Graph]:

        self.reset()
        for i in range(1, self.num_nodes + 1):
            if not self.visited[i]:
                self.dfs_solve(i, 0)

        res: List[Graph] = []
        for e in self.bridges:
            visited = [False] * (self.num_nodes + 1)
            g = [[] for _ in range(self.num_nodes + 1)]

            self.dfs_get_strong_components(e.v, 0, g, visited)

            res.append(Graph(g, self.num_nodes, self.num_edges))

        return res
