from collections import deque
from typing import List, Optional, Tuple, Dict, Set


class CheckpostsSolution:

    def __init__(self, m: int, n: int, costs: List[int], g: List[List[int]]):
        self.m: int = m
        self.n: int = n
        self.costs: List[int] = costs
        self.g: List[List[int]] = g

        self.low: List[int] = [0 for _ in range(n + 1)]
        self.num: List[int] = [0 for _ in range(n + 1)]
        self.time: int = 0

        self.free: List[bool] = [True for _ in range(n+1)]
        self.scc: List[List[int]] = []

        self.st: deque = deque()

    def dfs_solve(self, u: int):

        self.time += 1
        self.low[u] = self.num[u] = self.time

        self.st.append(u)

        for v in self.g[u]:

            if not self.free[v]:
                continue

            if self.num[v] == 0:
                self.dfs_solve(v)
                self.low[u] = min(self.low[u], self.low[v])
            else:
                self.low[u] = min(self.num[v], self.low[u])

        if self.low[u] == self.num[u]:
            self.crack_graph(u)

    def crack_graph(self, u: int):

        new_scc: List[int] = []

        cur_n = self.st.pop()
        new_scc.append(cur_n)
        self.free[cur_n] = False
        while cur_n != u:
            cur_n = self.st.pop()
            new_scc.append(cur_n)
            self.free[cur_n] = False

        self.scc.append(new_scc)

    def solve(self):

        self.time = 0
        self.st.clear()

        for u in range(1, self.n+1):
            if self.num[u] == 0:
                self.dfs_solve(u)

        min_total_cost = 0

        num_way: int = 1
        for scc in self.scc:

            min_cost = 10**9 + 7
            freq = 1
            for node in scc:
                if self.costs[node] < min_cost:
                    freq = 1
                    min_cost = self.costs[node]
                elif self.costs[node] == min_cost:
                    freq += 1

            min_total_cost += min_cost
            num_way *= freq

        return min_total_cost, num_way
    
