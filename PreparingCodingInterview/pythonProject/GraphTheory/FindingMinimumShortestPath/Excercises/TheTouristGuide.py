from typing import List
from collections import deque
import math


class TargetEdge:
    def __init__(self, v: int, c: int):
        self.v: int = v
        self.c: int = c


class TheTouristGuideSolution:
    def __init__(self, n: int, m: int, edges: List[tuple], s: int, d: int, t: int):
        self.n: int = n
        self.m: int = m
        self.edges: List[tuple] = edges
        self.s: int = s
        self.d: int = d
        self.t: int = t

    def solve(self) -> int:
        g: List[List[TargetEdge]] = [[] for _ in range(self.n+1)]

        for edge in self.edges:
            u, v, c = edge

            num_travel = math.ceil(self.t / c)
            g[u].append(TargetEdge(v, num_travel))
            g[v].append(TargetEdge(u, num_travel))

        q: deque = deque()

        in_queue: List[bool] = [False for _ in range(self.n + 1)]
        min_dist: List[int] = [10 ** 9 + 1 for _ in range(self.n + 1)]
        cnt: List[int] = [0 for _ in range(self.n + 1)]

        min_dist[self.s] = 0
        q.append(self.s)
        in_queue[self.s] = True

        while q:
            cur_n = q.popleft()
            in_queue[cur_n] = False

            cur_dist = min_dist[cur_n]
            for e in g[cur_n]:

                new_dist = cur_dist + e.c

                if new_dist < min_dist[e.v]:
                    min_dist[e.v] = new_dist

                    if not in_queue[e.v]:
                        q.append(e.v)
                        in_queue[e.v] = True

                        cnt[e.v] += 1

                        if cnt[e.v] > self.m:
                            return -1

        return min_dist[self.d]


n1, m1 = 7, 10

edge_str = '''1 2 30
1 3 15
1 4 10
2 4 25
2 5 60
3 4 40
3 6 20
4 7 35
5 7 20
6 7 30'''

edge_lines = edge_str.split('\n')

edges1 = []

for line in edge_lines:
    uvc = line.split(' ')
    edges1.append((int(uvc[0]), int(uvc[1]), int(uvc[2])))

s1, d1, t1 = 1, 7, 99
sln = TheTouristGuideSolution(n1, m1, edges1, s1, d1, t1)

print(sln.solve())
