from typing import List


class DSU:
    def __init__(self, size: int):
        self.par: List[int] = [i for i in range(size)]
        self.size: int = size
        self.rank: List[int] = [1 for _ in range(size)]

    def find(self, u: int):
        if u == self.par[u]:
            return u
        self.par[u] = self.find(self.par[u])
        return self.par[u]

    def merge(self, u: int, v: int) -> bool:
        par_u, par_v = self.find(u), self.find(v)

        if par_u == par_v:
            return False
        # if self.rank[par_u] < self.rank[par_v]:
        #     par_u, par_v = par_v, par_u
        # self.rank[par_u] += self.rank[par_v]
        self.par[par_v] = par_u
        return True
    def __str__(self):
        return str(self.par)

    def __repr__(self):
        return str([(i, self.par[i]) for i in range(self.size)])

class MinSwapsCouplesSolution:
    def __init__(self, row: List[int]):
        self.row = row

    def modeling_problem(self) -> List[List[int]]:

        double_n = len(self.row)
        n = double_n // 2
        graph: List[List[int]] = [[] for _ in range(n+1)]

        for idx in range(double_n):
            u = self.row[idx] // 2
            if idx > 0:
                v = self.row[idx-1] // 2
                graph[u].append(v)
            if idx < double_n-1:
                v = self.row[idx+1] // 2
                graph[u].append(v)
        return graph

    def solve(self) -> int:
        n = len(self.row)
        dsu = DSU(n//2)
        num_merge = 0
        for i in range(0,n, 2):
            u, v = self.row[i] // 2, self.row[i+1]//2
            if dsu.merge(v, u):
                num_merge += 1

        return num_merge

print(MinSwapsCouplesSolution([0, 5, 4, 1, 3, 2, 1, 5, 4, 3, 2, 0]).solve())
