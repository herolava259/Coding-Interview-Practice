from typing import List
from collections import deque

class DamageSolution:

    def __init__(self, n: int, m: int, g: List[List[int]], notifications: List[int]):
        self.n: int = n
        self.m: int = m
        self.g: List[List[int]] = g
        self.notifications: List[int] = notifications

    def bfs_solve(self):
        visited = [False for _ in range(self.n + 1)]
        no_path_fields = [False for _ in range(self.n + 1)]
        damaged = [False for _ in range(self.n + 1)]

        counter = 0
        for field in self.notifications:
            no_path_fields[field] = True
            for v in self.g[field]:
                damaged[v] = True

        visited[1] = True
        dq: deque = deque()
        dq.append(1)
        while dq:
            curr_node = dq.popleft()

            for v in self.g[curr_node]:

                if visited[v]:
                    continue

                if damaged[v] or no_path_fields[curr_node]:
                    no_path_fields[v] = True

                visited[v] = True

                if no_path_fields[v]:
                    dq.append(v)
                    counter += 1
                else:
                    dq.appendleft(v)

        return counter


