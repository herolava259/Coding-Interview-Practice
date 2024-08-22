from typing import List


def factorial(n):

    res = 1

    for i in range(1, n+1):
        res *= i
    return res

class ReformPlanSolution:
    def __init__(self, m: int, n: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g

        self.low: List[int] = [0 for _ in range(n+1)]
        self.num: List[int] = [0 for _ in range(n+1)]
        self.time: int = 0

        self.num_bridge: int = 0
        self.num_nodes: List[int] = []

    def dfs_solve(self, u: int, p: int):

        self.time += 1
        self.low[u] = self.num[u] = self.time
        self.num_nodes[-1] += 1

        for v in self.g[u]:
            if v == p:
                continue

            if self.num[v] == 0:

                self.dfs_solve(v, u)

                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] == self.num[v]:
                    self.num_bridge += 1

            else:
                self.low[u] = min(self.low[u], self.num[v])

    def solve(self) -> int:

        for u in range(1, self.n+1):
            if self.num[u] == 0:
                self.time = 0
                self.num_nodes.append(0)

                self.dfs_solve(u, 0)

        fac_n = factorial(self.n)
        res = 0
        if len(self.num_nodes) == 1:
            res = (fac_n - self.m) * (self.m - self.num_bridge)
        else:
            res = self.num_nodes[0] * self.num_nodes[1] * (self.m - self.num_bridge)

        return res

