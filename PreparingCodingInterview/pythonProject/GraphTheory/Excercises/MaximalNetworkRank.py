from typing import List


class MaximalNetworkRankSolution:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n: int = n
        self.roads: List[List[int]] = edges

    def solve(self) -> int:

        ranks: List[int] = [0] * self.n
        connected_mtx: List[List[bool]] = [[False] * self.n for _ in range(self.n)]
        for u, v in self.roads:
            ranks[u] += 1
            ranks[v] += 1
            connected_mtx[u][v] = connected_mtx[v][u] = True

        max_pair_rank: int = 0

        for u in range(self.n):
            for v in range(u + 1, self.n):
                pair_num_edges = ranks[u] + ranks[v]

                if connected_mtx[u][v]:
                    pair_num_edges -= 1

                if pair_num_edges > max_pair_rank:
                    max_pair_rank = pair_num_edges
        return max_pair_rank


n1 = 8
roads1 = roads = [[0, 1], [1, 2], [2, 3], [2, 4], [5, 6], [5, 7]]
sln = MaximalNetworkRankSolution(n1, roads1)

print(sln.solve())
