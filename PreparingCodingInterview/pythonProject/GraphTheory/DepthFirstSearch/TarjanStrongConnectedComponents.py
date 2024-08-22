from typing import List
from collections import deque


class TarjanSCCSolution:
    def __init__(self, m: int, n: int, g: List[List[int]]):
        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g
        self.low: List[int] = []
        self.num: List[int] = []
        self.time: int = 0

        self.frees: List[bool] = []

        self.scc: List[List[int]] = []

        self.s: deque = deque()

    def dfs_resolve(self, u: int, p: int):
        self.time += 1
        self.low[u] = self.num[u] = self.time

        self.s.append(u)

        for v in self.g[u]:
            if v == p:
                continue
            if not self.frees[v]:
                continue

            if self.num[v] == 0:
                self.dfs_resolve(v, u)
                self.low[u] = min(self.low[u], self.low[v])
            else:
                self.low[u] = min(self.num[v], self.low[u])

        if self.num[u] == self.low[u]:
            new_scc = self.crack_graph(u)
            self.scc.append(new_scc)

    def crack_graph(self, u: int) -> List[int]:

        sub_tree = []
        while self.s:
            curr_s = self.s.pop()
            sub_tree.insert(0, curr_s)
            self.frees[curr_s] = False
            if curr_s == u:
                break

        return sub_tree

    def solve(self) -> List[List[int]]:
        # init ds for proceed
        self.s.clear()
        self.time = 0
        self.num = [0 for _ in range(self.n+1)]
        self.low = [0 for _ in range(self.n+1)]
        self.frees = [True for _ in range(self.n+1)]

        for u in range(1, self.n+1):
            if self.num[u] == 0:
                self.dfs_resolve(u, -1)

        return self.scc

