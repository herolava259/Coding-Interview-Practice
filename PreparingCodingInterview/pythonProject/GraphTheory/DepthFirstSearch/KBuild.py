from typing import List


class Edge:
    def __init__(self, u: int, v: int):
        self.u: int = u
        self.v: int = v


class KBuildSolution:
    def __init__(self, m: int, n: int, g: List[List[int]], probed_schedules: List[tuple]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g
        self.schedules: List[tuple] = probed_schedules

        self.low: List[int] = [0 for _ in range(self.n + 1)]
        self.num: List[int] = [0 for _ in range(self.n + 1)]
        self.time: int = 0
        self.bridges: List[Edge] = []

    def dfs_explore(self, u: int, p: int = -1):

        self.time += 1
        self.low[u] = self.num[u] = self.time

        for v in self.g[u]:
            if v == p:
                continue

            if self.num[v] == 0:

                self.dfs_explore(v, u)

                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] == self.num[v]:
                    self.bridges.append(Edge(u, v))

            else:
                self.low[u] = min(self.low[u], self.num[v])

    def solve(self) -> List[Edge]:

        for u, v in self.schedules:
            if u not in self.g[v]:
                self.g[v].append(u)
            if v not in self.g[u]:
                self.g[u].append(v)

        self.dfs_explore(1, -1)

        return self.bridges

