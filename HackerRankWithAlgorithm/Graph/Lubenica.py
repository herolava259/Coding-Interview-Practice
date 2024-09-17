import os
import re
import math
import sys
from typing import List

inf = sys.maxint

class Data:
    def __init__(self, par: int, min_c:int=inf, max_c: int = -inf):
        self.max_c = max_c
        self.min_c = min_c
        self.par = par

class Edge:
    def __init__(self, v:int, c:int):
        self.v = v
        self.c = c

class LubenicaSolution:
    def __init__(self, g: List[List[Edge]], n: int):
        self.g = g
        self.n = n
        self.up: List[List[Data]] = [[Data(i) for _ in range(21)] for i in range(n)]
        self.h = [0 for _ in range(n)]
        self.q = 0

    def dfs(self, u: int, p: int):

        self.up[u][0].par = p

        for e in self.g[u]:

            if e.v != p:
                self.h[e.v] = self.h[u] + 1
                self.up[e.v][0].max_c = self.up[e.v][0].min_c = e.c
                self.dfs(e.v, u)

    def query(self, u:int, v:int) -> str:

        res: Data = Data(0)

        if self.h[u] < self.h[v]:
            u, v = v, u

        depth = self.h[u] - self.h[v]

        for i in range(20, -1, -1):
            if 1 & (depth >> i) == 1:
                res.max_c = max(res.max_c, self.up[u][i].max_c)
                res.min_c = min(res.min_c, self.up[u][i].min_c)
                u = self.up[u][i].par

        if u == v:
            return f'{res.min_c} {res.max_c}'

        for i in range(20, -1, -1):
            if self.up[i][i].par != self.up[v][i].par:

                res.max_c = max(res.max_c, self.up[u][i].max_c, self.up[v][i].max_c)
                res.min_c = max(res.min_c, self.up[u][i].min_c, self.up[v][i].min_c)
                u, v = self.up[u][i].par, self.up[v][i].par

        res.max_c = max(res.max_c, self.up[u][0].max_c, self.up[v][0].max_c)
        res.min_c = max(res.min_c, self.up[u][0].min_c, self.up[v][0].min_c)

        return f'{res.min_c} {res.max_c}'

    def build(self):
        self.dfs(1, 1)

        for i in range(1, 21):
            for u in range(1, self.n + 1):
                self.up[u][i].par = self.up[self.up[u][i-1].par][i-1].par
                self.up[u][i].max_c = max(self.up[u][i-1].max_c, self.up[self.up[u][i-1].par][i - 1].max_c)
                self.up[u][i].min_c = max(self.up[u][i - 1].min_c, self.up[self.up[u][i - 1].par][i - 1].min_c)


