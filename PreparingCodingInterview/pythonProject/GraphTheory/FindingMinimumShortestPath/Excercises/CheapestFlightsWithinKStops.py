from typing import List, Tuple, Deque as Queue
from collections import deque as queue

class FindCheapestPriceSolution:

    def __init__(self, n: int, flights: List[List[int]], src: int, dst: int, k: int):

        self.n: int = n
        self.flight: List[List[int]] = flights

        self.src: int = src
        self.dst: int = dst

        self.k: int = k

    def solve(self) -> int:

        if self.src == self.dst:
            return 0

        g: List[List[Tuple[int, int]]] = [[] for _ in range(self.n)]

        inf = (1 << 32) -1
        price: List[int] = [inf] * self.n

        for u, v, p in self.flight:

            g[u].append((v, p))


        price[self.src] = 0

        q: Queue[Tuple[int, int, int]] = queue()

        q.append((self.src, 0, 0))

        while q:
            u, num_stop, cost = q.popleft()
            for v, p in g[u]:
                estimation = cost + p

                if estimation < price[v]:
                    price[v] = estimation
                else:
                    continue
                if num_stop < self.k:
                    q.append((v, num_stop+1, estimation))

        return price[self.dst] if price[self.dst] < inf else -1

n1 = 11
flights1 = [[0,3,3],[3,4,3],[4,1,3],[0,5,1],[5,1,100],[0,6,2],[6,1,100],[0,7,1],[7,8,1],[8,9,1],[9,1,1],[1,10,1],[10,2,1],[1,2,100]]
src1 = 0
dst1 = 2
k1 = 4

sln = FindCheapestPriceSolution(n1, flights1, src1, dst1, k1)

print(sln.solve())
