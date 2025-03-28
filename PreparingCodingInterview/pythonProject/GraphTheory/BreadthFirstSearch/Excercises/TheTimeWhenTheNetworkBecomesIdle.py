from typing import List, Deque as Queue
from collections import deque as queue
import math

class NetworkBecomeIdleSolution:
    def __init__(self, edges: List[List[int]], patience: List[int]):

        self.edges: List[List[int]] = edges
        self.patience: List[int] = patience

    def solve(self) -> int:
        n: int = len(self.patience)
        g: List[List[int]] = [[] for _ in range(n)]

        for u, v in self.edges:
            g[u].append(v)
            g[v].append(u)

        def calc_time_exchange(interval: int, patience: int) -> int:

            cycle: int = interval << 1

            num_sending = math.ceil(cycle / patience)

            last_resending_time = patience * (num_sending-1)

            return last_resending_time + cycle

        path: List[int] = [0] * n
        visited: List[bool] = [False] * n
        last_receiving_time: int = 0
        q: Queue[int] = queue()
        visited[0] = True
        q.append(0)

        while q:
            u = q.popleft()

            for v in g[u]:
                if visited[v]:
                    continue

                visited[v] = True
                path[v] = path[u] + 1

                last_receiving_time = max(last_receiving_time,
                                          calc_time_exchange(path[v], self.patience[v]))
                q.append(v)

        return last_receiving_time + 1

edges1= [[0,1],[0,2],[1,2]]
patience1 = [0,10,10]

sln = NetworkBecomeIdleSolution(edges1, patience1)

print(sln.solve())

