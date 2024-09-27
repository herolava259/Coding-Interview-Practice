from typing import List


class FJBOfGraphSolution:

    def __init__(self, m: int, n: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g
        self.low: List[int] = [0 for _ in range(self.n + 1)]
        self.num: List[int] = [0 for _ in range(self.n + 1)]
        self.tail: List[int] = [0 for _ in range(self.n + 1)]
        self.time = 0
        self.root = 1
        self.joint: List[bool] = [False for _ in range(self.n + 1)]
        self.num_bridge = 0

    def dfs_find(self, u: int, p: int):

        self.time += 1
        self.low[u] = self.num[u] = self.tail[u] = self.time
        num_child = 0

        for v in self.g[u]:
            if v == p:
                continue

            if self.num[v] == 0:
                num_child += 1
                self.dfs_find(v, u)
                self.low[u] = min(self.low[u], self.low[v])

                if self.low[v] == self.num[v]:
                    self.num_bridge += 1
                if u == self.root:
                    if num_child > 1:
                        self.joint[u] = True
                elif self.low[v] >= self.num[u]:
                    self.joint[u] = True
            else:
                self.low[u] = min(self.low[u], self.num[v])

        self.tail[u] = self.time

    def solve(self) -> tuple:

        self.dfs_find(self.root, -1)
        num_joint = 0

        for is_joint in self.joint:
            if is_joint:
                num_joint += 1

        return self.num_bridge, num_joint
