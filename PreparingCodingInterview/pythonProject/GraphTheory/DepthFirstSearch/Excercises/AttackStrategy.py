from typing import List


class AttackStrategySolution:

    def __init__(self, m: int, n: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g

        self.low: List[int] = [0 for _ in range(self.n + 1)]
        self.num: List[int] = [0 for _ in range(self.n + 1)]

        self.time: int = 0
        self.joint: List[bool] = [False for _ in range(self.n + 1)]
        self.root = 1

    def dfs_solve(self, u: int, p: int = 0):

        self.time += 1

        self.low[u] = self.num[u] = self.time
        num_child = 0
        for v in self.g[u]:
            if v == p:
                continue

            if self.num[v] == 0:

                self.dfs_solve(v, u)
                self.low[u] = min(self.low[u], self.low[v])
                if num_child > 0 and u == self.root:
                    self.joint[u] = True
                elif self.num[u] > self.low[v]:
                    self.joint[u] = True
            else:
                self.low[u] = min(self.low[u], self.num[v])

    def solve(self) -> int:

        self.dfs_solve(self.root)
        point_res = -1
        max_comp = 0

        for u in range(1, self.n + 1):
            if self.joint[u]:
                if max_comp < len(self.g[u]):
                    max_comp = len(self.g[u])
                    point_res = u

        return point_res
