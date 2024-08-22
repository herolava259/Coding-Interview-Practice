from typing import List


class NKPoliceSolution:
    def __init__(self, m: int, n: int, g: List[List[int]]):

        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g

        self.time: int = 0
        self.low: List[int] = [0 for _ in range(self.n + 1)]
        self.num: List[int] = [0 for _ in range(self.n + 1)]
        self.tail: List[int] = [0 for _ in range(self.n + 1)]
        self.joint: List[int] = [False for _ in range(self.n + 1)]
        self.root: int = 1
        self.depth: List[int] = [0 for _ in range(self.n + 1)]
        self.par: List[List[int]] = [[0 for _ in range(22)] for _ in range(self.n + 1)]
        self.bridges: List[set] = [set() for _ in range(self.n + 1)]

    def dfs_build(self, u: int, p: int = -1):

        num_child = 0
        self.time += 1
        if p != -1:
            self.depth[u] = self.depth[p] + 1
        self.par[u][0] = p
        self.low[u] = self.num[u] = self.tail[u] = self.time

        for v in self.g[u]:

            if v == p:
                continue

            if self.num[v] == 0:
                num_child += 1
                self.dfs_build(v, u)
                self.low[v] = min(self.low[u], self.low[v])

                if self.low[v] == self.num[v]:
                    self.bridges[v].add(u)
                    self.bridges[u].add(v)

                if p == -1:
                    if num_child > 1:
                        self.joint[u] = True
                elif self.low[v] >= self.num[u]:
                    self.joint[u] = True
            else:
                self.low[u] = min(self.low[u], self.num[v])

        self.tail[u] = self.time

    def calc_par(self):

        self.par[self.root][0] = self.root

        for j in range(1, 22):

            for u in range(1, self.n+1):
                self.par[u][j] = self.par[self.par[u][j-1]][j-1]

    def find_par(self, u: int, p: int):

        for i in range(21, -1, -1):
            if self.depth[p] < self.depth[self.par[u][i]]:
                u = self.par[u][i]

        return u

    def in_sub_tree(self, root: int, u: int) -> bool:
        return self.num[root] <= self.num[u] <= self.tail[u]

    def query_road(self, a: int, b: int, road: tuple) -> bool:

        g1, g2 = road

        if g2 not in self.bridges[g1] or g1 not in self.bridges[g2]:
            return False

        if self.num[g1] > self.num[g2]:
            g1, g2 = g2, g1

        if self.in_sub_tree(g2, a) and not self.in_sub_tree(g2, b):
            return True
        if not self.in_sub_tree(g2, a) and self.in_sub_tree(g2, b):
            return True

        return False

    def query_city(self, a: int, b: int, c: int) -> bool:

        if not self.joint[c]:
            return False

        pa = 1
        pb = 1

        if self.in_sub_tree(c, a):
            pa = self.find_par(a, c)
        if self.in_sub_tree(c, b):
            pb = self.find_par(b, c)

        if pa == pb:
            return False

        if self.low[pa] < self.num[c] and self.low[pb] < self.num[c]:
            return False

        return True
