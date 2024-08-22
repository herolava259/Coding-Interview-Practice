from typing import List

"""
save data about component contain a and component contain b if edge's created by nodes a and b 
is bridge 

component include nodes and edges between them 

"""


class WeatherSolution:

    def __init__(self, n: int, m: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n

        self.g: List[List[int]] = g

        self.low: List[int] = [0 for _ in range(self.n + 1)]
        self.num: List[int] = [0 for _ in range(self.n + 1)]
        self.tail: List[int] = [0 for _ in range(self.n + 1)]
        self.par: List[List[int]] = [[0 for _ in range(32)] for _ in range(self.n + 1)]
        self.time = 0
        self.bridges: List[tuple] = []
        self.root: List[int] = [0 for _ in range(self.n + 1)]

    def dfs_solve(self, u: int, p: int, root: int):

        self.par[u][0] = p
        self.root[u] = root
        self.time += 1
        self.num[u] = self.low[u] = self.time

        for v in self.g[u]:
            if v == p:
                continue

            if self.num[u] == 0:
                self.dfs_solve(v, u, root)

                if self.low[v] == self.num[v]:
                    self.bridges.append((u, v))
                self.low[u] = min(self.low[u], self.low[v])
            else:
                self.low[u] = min(self.num[v], self.low[u])
        self.tail[u] = self.time

    def build_parent(self):

        for j in range(1, 32):
            for u in range(1, self.n + 1):
                self.par[u][j] = self.par[self.par[u][j - 1]][j - 1]

    def build(self):

        for u in range(1, self.n + 1):
            if self.num[u] == 0:
                self.time = 0
                self.root[u] = u
                self.dfs_solve(u, 0, u)

        self.build_parent()

    def find_par(self, u: int, p: int):

        if not (self.num[p] <= self.num[u] <= self.tail[p]):
            return self.par[u][0]

        anc_u = u

        for i in range(31, -1, -1):
            if self.num[self.par[anc_u][i]] < self.num[p]:
                anc_u = self.par[anc_u][i]

        return anc_u

    def solve(self) -> int:

        res: int = 0

        for bridge in self.bridges:
            u, v = bridge
            prev_bridge = self.num[u] - 1
            post_bridge = self.tail[self.root[v]] - self.num[v]

            res += prev_bridge * post_bridge

        return res
