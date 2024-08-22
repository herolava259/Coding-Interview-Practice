from typing import List


class BuildingEulerPathInTree:
    def __init__(self, n: int, m: int, g: List[List[int]]):
        self.m = m
        self.n = n
        self.g = g
        self.time = 0
        self.starts: List[int] = [0 for _ in range(self.n + 1)]
        self.ends: List[int] = [0 for _ in range(self.n + 1)]
        self.tour: List[int] = []
        self.h: List[int] = [0 for _ in range(self.n + 1)]
        self.root = 1

    def add(self, u: int):
        self.time += 1
        self.tour.append(u)
        self.ends[u] = self.time

    def dfs(self, u: int, p: int):
        self.h[u] = self.h[p] + 1

        self.add(u)
        self.starts[u] = self.time

        for v in self.g[u]:
            if v != p:
                self.dfs(v, u)

        if u != self.root:
            self.add(p)

    def solve(self) -> List[int]:

        self.time = 0
        self.tour = []

        self.dfs(self.root, -1)

        return self.tour

class SimpliedBuildingEulerPathInTree:
    def __init__(self, n: int, m: int, g: List[List[int]]):
        self.m = m
        self.n = n
        self.g = g
        self.time = 0
        self.starts: List[int] = [0 for _ in range(self.n + 1)]
        self.ends: List[int] = [0 for _ in range(self.n + 1)]
        self.tour: List[int] = []
        self.h: List[int] = [0 for _ in range(self.n + 1)]
        self.root = 1

    def add(self, u: int):
        self.time += 1
        self.tour.append(u)
        self.ends[u] = self.time

    def dfs(self, u: int, p: int):
        self.h[u] = self.h[p] + 1

        self.add(u)
        self.starts[u] = self.time

        for v in self.g[u]:
            if v != p:
                self.dfs(v, u)

        self.ends[u] = self.time

    def solve(self) -> List[int]:

        self.time = 0
        self.tour = []

        self.dfs(self.root, -1)

        return self.tour