from typing import List, Tuple
from heapq import heappush, heappop


class MinTimeToReachIISolution:
    def __init__(self, move_time: List[List[int]]):
        self.move_time: List[List[int]] = move_time

        self.n_row = len(self.move_time)
        self.m_col = len(self.move_time[0])

    def solve(self) -> int:

        adjacent_offsets: List[Tuple[int, int]] = [(0,1), (0, -1), (1, 0), (-1, 0)]

        d: List[List[int]] = [[10**12+12] * self.m_col for _ in range(self.n_row)]

        visited: List[List[bool]] = [[False] * self.m_col for _ in range(self.n_row)]

        pq: List[Tuple[int, int, int, bool]] = [(0, 0, 0, False)]

        def calc_time(i_row: int, j_col: int, stripe: bool,  cur_time: int):
            return max(self.move_time[i_row][j_col], cur_time) + (1 if not stripe else 2)

        while pq:
            cur_d, u_row, u_col, cur_stripe = heappop(pq)

            if visited[u_row][u_col]:
                continue
            visited[u_row][u_col] = True

            for offset_row, offset_col in adjacent_offsets:
                adj_row, adj_col = u_row + offset_row, u_col + offset_col

                if not 0 <= adj_row < self.n_row or not 0 <= adj_col < self.m_col:
                    continue
                if visited[adj_row][adj_col]:
                    continue
                try_d = calc_time(adj_row, adj_col, cur_stripe, cur_d)

                if try_d < d[adj_row][adj_col]:
                    d[adj_row][adj_col] = try_d
                    heappush(pq, (try_d, adj_row, adj_col, not cur_stripe))

        return d[-1][-1]


moveTime = [[0,0,0,0],[0,0,0,0]]

print(MinTimeToReachIISolution(moveTime).solve())