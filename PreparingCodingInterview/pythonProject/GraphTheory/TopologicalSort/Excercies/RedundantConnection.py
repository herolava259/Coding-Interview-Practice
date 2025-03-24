from typing import List

class DSU:
    def __init__(self, n: int):

        self.par: List[int] = list(range(n+1))
        self.n: int = n

    def find_par(self, u) -> int:
        if self.par[u] == u:
            return u
        self.par[u] = self.find_par(self.par[u])

        return self.par[u]

    def join(self, u: int, v: int) -> bool:

        par_u: int = self.find_par(u)
        par_v: int = self.find_par(v)

        if par_u == par_v:
            return False

        self.par[par_v] = par_u

        return True

class RedundantConnectionSolution:
    def __init__(self, edges: List[List[int]]):

        self.edges: List[List[int]] = edges
        self.n: int = len(self.edges)

    def solve(self) -> List[int]:

        u, v = 1, 2

        dsu: DSU = DSU(self.n)

        for edge in self.edges:
            u,v = edge
            if not dsu.join(u, v):
                break

        return [u, v]

