
from typing import List


class SecureNetworkSolution:

    def __init__(self, m: int, n: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g

        self.low: List[int] = [0 for _ in range(self.n+1)]
        self.num: List[int] = [0 for _ in range(self.n+1)]
        self.components: List[int] = []

        self.time: int = 0

    def dfs_solve(self, u: int, p: int) -> int:

        self.time += 1
        self.low[u] = self.num[u] = self.time

        num_node = 1

        for v in self.g[u]:
            if v == p:
                continue

            if self.num[v] == 0:

                num_child = self.dfs_solve(v, u)

                self.low[u] = min(self.low[v], self.low[u])

                if self.low[v] < self.num[v]:
                    #(u,v) is not bridge
                    num_node += num_child
                elif self.low[v] == self.num[v]:
                    self.components.append(num_child)
            else:
                self.low[u] = min(self.low[u], self.num[v])

        return num_node

    def solve(self) -> int:

        for u in range(1, self.n+1):
            if self.num[u] == 0:
                self.time = 0
                num_node = self.dfs_solve(u, 0)
                self.components.append(num_node)

        return max(self.components)
