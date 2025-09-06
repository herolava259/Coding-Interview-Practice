from typing import List, Tuple


class DSU:
    def __init__(self,n: int):
        self.n: int = n
        self.par: List[int] = list(range(n))

    def find(self, u: int) -> int:
        if u == self.par[u]:
            return u
        self.par[u] = self.find(self.par[u])

        return self.par[u]

    def join(self, u: int, v: int) -> bool:
        par_u, par_v = self.find(u), self.find(v)

        if par_u == par_v:
            return False

        self.par[par_v] = par_u

        return True


def manhattan_distance(a: List[int], b: List[int]):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


class MinCostConnectPointsSolution:
    def __init__(self, points: List[List[int]]):
        self.points = points

    def solve(self) -> int:
        dsu = DSU(len(self.points))

        n = len(self.points)

        min_cost = 0

        edges: List[Tuple[int, int, int]] = []
        for u in range(n):
            for v in range(u+1, n):
                edges.append((manhattan_distance(self.points[u], self.points[v]), u, v))

        edges.sort()

        for _ in range(n-1):
            while edges:
                dist, u, v = edges.pop(0)
                if dsu.join(u,v):
                    min_cost += dist
                    break


        return min_cost


points = [[3,12],[-2,5],[-4,1]]

print(MinCostConnectPointsSolution(points).solve())
