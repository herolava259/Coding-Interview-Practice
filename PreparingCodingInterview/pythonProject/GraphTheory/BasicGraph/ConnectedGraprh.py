from typing import List
from collections import deque


class WarshalSolution:

    def __init__(self, adj_table: List[List[bool]]):
        self.num_node = len(adj_table)
        self.matrix = adj_table

    def solve(self) -> bool:
        for k in range(self.num_node):
            for u in range(self.num_node):
                if k != u and self.matrix[u][k]:
                    for v in range(self.num_node):
                        if u != v and v != k and self.matrix[k][v]:
                            self.matrix[u][v] = True
                            self.matrix[v][u] = True

        return WarshalSolution.is_fully_connected_graph(self.matrix)

    @staticmethod
    def is_fully_connected_graph(matrix: List[List[bool]]) -> bool:
        for row in matrix:
            for val in row:
                if not val:
                    return False
        return True


class TarjanSolution:

    def __init__(self, g: List[List[int]], n: int, m: int):
        self.g = g
        self.n = n
        self.m = m
        self.nums = [0 for _ in range(n + 1)]
        self.lowers = [0 for _ in range(n + 1)]
        self.frees = [False for _ in range(n + 1)]
        self.s = deque()
        self.time = 0
        self.res: List = []
        self.scc = 0

    def visit(self, u: int, p: int):

        self.time += 1
        self.lowers[u] = self.nums[u] = self.time

        self.s.append(u)

        for v in self.g[u]:
            if v == p:
                continue
            if self.frees[v]:
                continue
            if self.nums[v] == 0:
                self.visit(v, p)
            if not self.frees[v]:
                self.lowers[u] = min(self.lowers[u], self.lowers[v])

        if self.lowers[u] == self.nums[u]:

            sc = []
            while True:
                v = self.s.pop()
                sc.append(v)
                self.frees[v] = True
                if u == v:
                    break

            self.scc += 1
            self.res.append(sc)


class ExtendFindStrongComponentSolution:

    def __init__(self, g: List[List[int]], n, m):

        self.g = g
        self.num_edges = m
        self.num_vertex = n
        self.reverse_g = [[] for _ in range(n + 1)]
        self.nums = [0 for _ in range(n)]
        self.time = 0
        self.orders = [0 for _ in range(n + 1)]
        self.frees = [False for _ in range(n + 1)]
        self.res = []

    def create_reverse_g(self):
        for u in range(1, self.num_vertex + 1):
            for v in self.g[u]:
                self.reverse_g[v].append(u)

    def dfs_down(self, u, p):
        self.time += 1
        self.nums[u] = self.time
        self.orders[self.time] = u

        for v in self.g[u]:
            if v == p:
                continue

            if self.nums[u] > 0:
                self.dfs_down(u, v)

    def dfs_up(self, u: int) -> List[int]:

        res = []
        self.frees[u] = True
        for v in self.reverse_g[u]:
            if self.frees[v]:
                continue
            tmp = self.dfs_up(v)
            res.extend(tmp)
        return res

    def solve(self) -> List[List[int]]:
        self.create_reverse_g()
        self.dfs_down(1, 0)

        for u in self.orders:
            if not self.frees[u]:
                self.res.append(self.dfs_up(u))

        return self.res
