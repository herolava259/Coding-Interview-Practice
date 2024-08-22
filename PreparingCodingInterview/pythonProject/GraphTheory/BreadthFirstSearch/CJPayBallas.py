from typing import List
from queue import Queue

class CJPayBallSolution:
    def __init__(self, m: int, n: int, g: List[List[int]], s: int, t: int):
        self.m: int = m
        self.n: int = n
        self.g: List[List[int]] = g
        self.s: int = s
        self.t: int = t

    def bfs_solve(self) -> (int, List[int]):

        for u in range(1, self.n+1):
            self.g[u].sort()

        path: List[int] = []
        d_min = 0

        visited = [False for _ in range(self.n+1)]
        prev: List[int] = [0 for _ in range(self.n + 1)]

        q: Queue = Queue(maxsize= self.n + 1)
        q.put(self.s)
        visited[self.s] = True

        curr_node = self.s
        while not q.empty():
            curr_node = q.get()

            if curr_node == self.t:
                break

            for v in self.g[curr_node]:
                if visited[v]:
                    continue
                q.put(v)
                visited[v] = True
                prev[v] = curr_node

        if curr_node != self.t:
            return -1, None
        while curr_node != self.s:
            path.insert(0, curr_node)
            d_min += 1
            curr_node = prev[curr_node]
        path.insert(0, curr_node)

        return d_min, path





