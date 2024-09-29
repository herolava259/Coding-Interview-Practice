from typing import List


class CriticalConnectionSolution:
    def __init__(self, n: int, connections: List[List[int]]):
        self.n: int = n
        self.connections: List[List[int]] = connections
        self.g: List[List[int]] = [[] for _ in range(self.n)]
        self.low: List[int] = [0] * self.n
        self.num: List[int] = [0] * self.n
        self.time: int = 0
        self.bridges: List[List[int]] = []

    def dfs_find_bridge(self, u: int, p: int):
        self.time += 1
        self.low[u] = self.num[u] = self.time

        for v in self.g[u]:
            if v == p:
                continue
            if self.num[v] == 0:
                self.dfs_find_bridge(v, u)
                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] == self.num[v]:
                    self.bridges.append([u, v])
            else:
                self.low[u] = min(self.low[u], self.num[v])

    def build_graph(self):
        for u, v in self.connections:
            self.g[u].append(v)
            self.g[v].append(u)

    def solve(self) -> List[List[int]]:
        self.build_graph()

        for u in range(self.n):
            if self.num[u] == 0:
                self.time = 0
                self.dfs_find_bridge(u, -1)

        return self.bridges


connections1 = [[0,1]]
n1 = 2

sln = CriticalConnectionSolution(n1, connections1)

print(sln.solve())

