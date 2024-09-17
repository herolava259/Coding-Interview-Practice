import os
import re
import math
from typing import List

class Edge:

    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

class Dsu:

    def __init__(self, num_vertex: int):
        self.num_vertex = num_vertex
        self.parents = [0 for i in range(self.num_vertex + 5)]

        for i in range(self.num_vertex):
            self.parents[i] = i

    def reset(self):
        self.parents = [0 for i in range(self.num_vertex + 5)]

        for i in range(self.num_vertex):
            self.parents[i] = i

    def find(self, u: int) -> int:
        if self.parents[u] == u:
            return u

        self.parents[u] = self.find(self.parents[u])

        return self.parents[u]

    def join(self, u: int, v: int) -> bool:
        par_u, par_v = self.find(u), self.find(v)

        if par_u == par_v:
            return False

        self.parents[v] = u

        return True


class NKCitySolution:

    @staticmethod
    def solve(graph: List[Edge], num_vertex: int)-> int:
        graph.sort(key=lambda e: e.c)
        dsu = Dsu(num_vertex = num_vertex)
        max_weight = 0
        for edge in graph:
            if not dsu.join(edge.u, edge.v):
                continue

            max_weight = max(max_weight, edge.c)

        return max_weight