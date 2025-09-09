from typing import List
from collections import deque


class TopologicalSortSolution:

    def __init__(self, g: List[List[int]], n: int, m: int):

        self.n = n
        self.m = m
        self.g: List[List[int]] = g
        self.in_degrees: List[int] | None = None
        self.orders: List[int] = []

    def initialize(self):

        self.in_degrees = [0 for _ in range(self.n + 1)]
        for u in range(self.n + 1):
            for v in self.g[u]:
                self.in_degrees[v] += 1

    def solve(self) -> List[int]:

        q: deque = deque(self.find_in_zero_nodes())

        orders: List[int] = []
        while len(q) != 0:
            u = q.popleft()
            orders.append(u)
            for v in self.g[u]:
                self.in_degrees[v] -= 1

                if self.in_degrees[v] <= 0:
                    q.append(v)

        self.orders = orders

        return orders

    def find_in_zero_nodes(self) -> List[int]:
        res: List[int] = []
        for i in range(self.n + 1):
            if self.in_degrees[i] == 0:
                res.append(i)
        return res


class TopologicalBaseOnDFSSolution:
    def __init__(self, g: List[List[int]]):

        self.n = len(g)
        self.g: List[List[int]] = g
        self.states: List[int] = [0] * (self.n+1)
        self.orders: List[int] = []

    def dfs_solve(self, u: int, p: int = -1) -> bool:

        self.states[u] = 1
        for v in self.g[u]:
            if v == p:
                continue

            if self.states[v] == 1:
                return False
            if self.states[v] == 2:
                continue
            if not self.dfs_solve(v, u):
                return False

        self.states[u] = 2
        self.orders.append(u)
        return True

    def solve(self) -> List[int] | None:

        for i in range(self.n + 1):
            self.states[i] = 0
        self.orders = []

        for u in range(self.n + 1):
            if self.states[u] == 0:
                if not self.dfs_solve(u):
                    return None

        self.orders = self.orders[::-1]

        return self.orders
