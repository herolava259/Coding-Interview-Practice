from typing import List
import os
import math

class Edge:
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

class Dsu:
    def __init__(self, edges: List[Edge],num_vertex:int, pars: List[int] = []):
        self.edges = edges
        self.parents = pars
        self.num_edge = len(edges)
        self.num_vertex = num_vertex
        self.reset()

    def reset(self):
        self.parents = [0 for i in range(self.num_edge)]

    def find_root(self,u: int) -> int:
        if self.parents[u] == u:
            return u
        self.parents[u] = self.find_root(self.parents[u])

        return self.parents[u]

    def join_dsu(self, u: int, v: int) -> bool:
        u, v = self.find_root(u), self.find_root(v)
        if u == v:
            return False

        self.parents[v] = u

        return True


