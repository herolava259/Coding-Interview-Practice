from typing import List
import math


class NaiveLCASolution:
    def __init__(self, g: List[List[int]], root: int):

        self.g = g
        self.root = root
        self.n = len(g)
        self.parents: List[int] = [0 for _ in range(self.n + 1)]
        self.h: List[int] = [0 for i in range(self.n + 1)]

    def initialize(self):
        self.parents[self.root] = -1
        self.dfs_build(self.root, -1)

    def dfs_build(self, u: int, p: int):
        self.parents[u] = p
        if p != -1:
            self.h[u] = self.h[p] + 1
        else:
            self.h[u] = 0
        for v in self.g[u]:
            if v != p:
                self.dfs_build(v, u)

    def lca(self, u, v) -> int:
        if self.h[u] < self.h[v]:
            u, v = v, u

        while self.h[u] > self.h[v]:
            v = self.parents[v]

        while u != v:
            u = self.parents[u]
            v = self.parents[v]

        return u


class Improved1LCASolution:

    def __iter__(self, g: List[List[int]], root: int, h: int):
        self.root = root
        self.g = g
        self.n = len(g)
        self.parents: List[int] = [-1 for _ in range(self.n + 1)]
        self.h: int = h
        self.sqrt_h: int = int(math.sqrt(h))
        self.heights = [0 for _ in range(self.n + 1)]
        self.ancestors = [-1 for _ in range(self.n + 1)]

    def dfs_build(self, u: int, p: int, anc: int):
        self.parents[u] = p
        if p != -1:
            self.heights[u] = self.heights[p] + 1
        else:
            self.heights[u] = 0

        if self.heights[u] % anc == 0:
            self.ancestors[u] = anc
            anc = u
        else:
            self.ancestors[u] = anc

        for v in self.g[u]:
            if v != p:
                self.dfs_build(v, u, anc)

    def initialize(self):
        self.dfs_build(self.root, -1, self.root)

    def lca_query(self, u: int, v: int) -> int:

        while self.ancestors[u] != self.ancestors[v]:
            if self.h[u] > self.h[v]:
                u = self.ancestors[u]
            else:
                v = self.ancestors[v]

        while u != v:
            if self.heights[u] > self.heights[v]:
                u = self.parents[u]
            else:
                v = self.parents[v]

        return u


class SparseTableLCASolution:
    def __init__(self, g: List[List[int]], root: int):
        self.root = root
        self.g = g
        self.n = len(g)
        self.parents: List[List[int]] | None = None
        self.h: List[int] = [0 for _ in range(self.n + 1)]

    def dfs_build(self, u, p):

        if p == -1:
            self.h[u] = 0
        else:
            self.h[u] = self.h[p] + 1
        self.parents[u][0] = p

        for v in self.g[u]:
            if v != p:
                self.dfs_build(v, p)

    def initialize(self):

        if self.parents is not None:
            return
        upper_log2 = math.ceil(math.log(self.n, 2))
        self.parents = [[-1 for _ in range(upper_log2)] for _ in range(self.n + 1)]
        self.dfs_build(self.root, -1)

        for j in range(1, upper_log2):
            for u in range(self.n + 1):
                if 1 << j > self.h[u]:
                    self.parents[u][j] = -1
                    continue
                self.parents[u][j] = self.parents[self.parents[u][j - 1]][j - 1]

    def lca_query(self, u: int, v: int):
        if self.h[u] > self.h[v]:
            u, v = v, u

        diff_h = self.h[v] - self.h[u]

        while diff_h > 0:
            offset = diff_h & (-diff_h)
            v = self.parents[v][offset]
            diff_h &= (diff_h - 1)

        if u == v:
            return u
        log_h = int(math.log(self.h[u], 2))

        for i in range(log_h, -1, -1):
            if self.parents[u][i] != -1 and self.parents[u][i] != self.parents[v][i]:
                u = self.parents[u][i]
                v = self.parents[v][i]

        return self.parents[u][0]
