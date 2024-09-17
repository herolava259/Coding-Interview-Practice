from typing import List
from collections import deque


class NumberOfRoadsSolution:

    def __init__(self, roads: List[List[int]]):

        self.roads: List[List[int]] = roads

        self.m = len(self.roads)

        n = 0

        for u, v in self.roads:
            n = max(n, u, v)

        self.n = n

        self.g: List[List[int]] = [[] for _ in range(self.n + 1)]
        self.visited: List[bool] = [False for _ in range(self.n + 1)]
        self.nums = 0
        for u, v in self.roads:
            self.g[u].append(v)
            self.g[v].append(u)

    def solve(self) -> int:

        for i in range(1, self.n):
            for j in range(i+1, self.n):
                for k in range(j+1, self.n):
                    dist01 = self.calc_dist(i, j)
                    dist12 = self.calc_dist(j, k)
                    dist20 = self.calc_dist(k, i)
                    if dist01 == dist12 and dist12 == dist20:
                        self.nums += 1

        return self.nums

    def backtrack(self, cities: List[int],beg: int = 0, k: int = 1,):

        if k == 4:
            dist01 = self.calc_dist(cities[0], cities[1])
            dist12 = self.calc_dist(cities[1], cities[2])
            dist20 = self.calc_dist(cities[2], cities[0])
            if dist01 == dist12 and dist12 == dist20:
                self.nums += 1
                return
            else:
                return

        for i in range(beg, self.n + 1):
            if self.visited[i]:
                continue
            cities.append(i)
            self.visited[i] = True
            self.backtrack(cities, i+1, k + 1)
            self.visited[i] = False
            cities.pop()

    def calc_dist(self, u: int, v: int) -> int:

        visited: List[bool] = [False for _ in range(self.n + 1)]

        cur_d, cur_n = 0, u
        visited[u] = True

        q: deque = deque()

        q.append((cur_d, cur_n))

        while q:
            cur_d, cur_n = q.popleft()

            if cur_n == v:
                return cur_d

            for nei in self.g[cur_n]:

                if visited[nei]:
                    continue

                visited[nei] = True

                q.append((cur_d + 1, nei))

        return 0
