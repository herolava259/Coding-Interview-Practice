from typing import List

class Edge:
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

class DSU:
    def __init__(self, n: int):
        self.n: int = n
        self.par: List[int] = [i for i in range(self.n + 5)]

    def find(self, u: int) -> int:
        if self.par[u] == u:
            return u
        self.par[u] = self.find(self.par[u])
        return self.par[u]

    def join(self, u: int, v: int):
        u = self.find(u)
        v = self.find(v)

        if u == v:
            return False

        self.par[v] = u

        return True
