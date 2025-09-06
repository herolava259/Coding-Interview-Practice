from typing import List, Tuple
import heapq

class MinTimeToReachSolution:
    def __init__(self, move_time: List[List[int]]):
        self.move_time: List[List[int]] = move_time
        self.n_row = len(self.move_time)
        self.m_col = len(self.move_time[0])

    def solve(self) -> int:

        adjacent_offset = [(0,1), (0,-1), (1, 0), (-1, 0)]


        d: List[List[int]] = [[10**12+7] * self.m_col for _ in range(self.n_row)]

        d[0][0] = 0

        pq: List[Tuple[int, int, int]] = [(0, 0, 0)]

        released: List[List[bool]] = [[False] * self.m_col for _ in range(self.n_row)]

        def calc_time(i_row, i_col, cur_time):
            return max(self.move_time[i_row][i_col], cur_time) + 1

        while pq:
            cur_d, u_row, u_col = heapq.heappop(pq)

            if released[u_row][u_col]:
                continue
            released[u_row][u_col] = True

            for offset_row, offset_col in adjacent_offset:
                adj_row, adj_col = u_row + offset_row, u_col + offset_col
                if not 0 <= adj_row < self.n_row or not 0 <= adj_col < self.m_col:
                    continue
                if released[adj_row][adj_col]:
                    continue

                try_d = calc_time(adj_row, adj_col, cur_d)
                if try_d < d[adj_row][adj_col]:
                    d[adj_row][adj_col] = try_d
                    heapq.heappush(pq, (try_d, adj_row, adj_col))


        return d[-1][-1]


moveTime = [[0,1],[1,2]]


print(MinTimeToReachSolution(moveTime).solve())
