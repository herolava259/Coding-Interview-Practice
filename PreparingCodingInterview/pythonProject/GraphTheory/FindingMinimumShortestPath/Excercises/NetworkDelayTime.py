from typing import List, Tuple
import heapq

class NetworkDelayTimeSolution:

    def __init__(self, times: List[List[int]], n: int, k: int):

        self.times:List[List[int]] = times
        self.n: int = n
        self.k: int = k

    def dijikstra_solve(self) -> int:

        m_edge = len(self.times)
        infinity = (1 << 32) - 1
        visited: List[bool] = [False] * (self.n+1)

        path: List[int] = [infinity] * (self.n+1)

        adj: List[List[Tuple[int, int]]] = [[] for _ in range(self.n+1)]

        pq: List[Tuple[int, int]] = []

        num_visited = 0

        for u, v, w in self.times:
            if u == self.k:
                path[v] = w
                heapq.heappush(pq, (w, v))
            adj[u].append((v, w))

        max_time = -1

        while pq:
            _, u = heapq.heappop(pq)
            if visited[u]:
                continue
            visited[u] =True
            num_visited += 1
            max_time = path[u]
            for v, w in adj[u]:
                if visited[v]:
                    continue
                if v == self.k and path[u] < path[v]:
                    path[v] = path[u]
                    heapq.heappush(pq, (path[v], v))
                    continue
                if path[u] + w < path[v]:
                    path[v] = path[u] + w
                    heapq.heappush(pq, (path[v], v))

        if num_visited < self.n - 1:
            return -1

        if num_visited == self.n - 1 and visited[self.k]:
            return -1

        return max_time


times1 = [[2,1,1],[2,3,1],[3,4,1]]
n1 = 4
k1 = 2

sln = NetworkDelayTimeSolution(times1, n1, k1)

print(sln.dijikstra_solve())