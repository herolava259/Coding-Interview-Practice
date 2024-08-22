from typing import List
from collections import deque

map_offset = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}


class OceanCurrentsSolution:
    def __init__(self, m_row: int, n_col, matrix: List[List[int]], s: tuple, d: tuple):
        self.m_row: int = m_row
        self.n_col: int = n_col
        self.mtx: List[List[int]] = matrix
        self.s: tuple = s
        self.d: tuple = d

    def bfs_solve(self) -> int:

        dq: deque = deque()
        curr_cost = 0
        cur_x, cur_y = self.s
        end_x, end_y = self.d

        dq.appendleft((cur_x, cur_y, curr_cost))

        d_cost = [[100_000_007 for _ in range(self.n_col)] for _ in range(self.m_row)]
        d_cost[cur_x][cur_y] = 0
        while dq:

            cur_x, cur_y, curr_cost = dq.popleft()

            if cur_x == end_x and cur_y == end_y:
                return curr_cost

            dir_no_cost = self.mtx[cur_x][cur_y]
            offset_x, offset_y = map_offset[dir_no_cost]

            pos = (cur_x, cur_y)
            exclude = (offset_x, offset_y)

            if self.update_to_enqueue((2, 2), exclude, pos, d_cost, 0):
                dq.appendleft((cur_x + offset_x, cur_y + offset_y, curr_cost))

            for new_offset in map_offset.values():
                if self.update_to_enqueue(exclude, new_offset, pos, d_cost):
                    dq.append((cur_x + new_offset[0], cur_y + new_offset[1], curr_cost + 1))

        return -1

    def update_to_enqueue(self, exclude: tuple, offset: tuple, pos: tuple, curr_d_cost, cost_cell=1) -> bool:

        exclude_x, exclude_y = exclude
        offset_x, offset_y = offset
        pos_x, pos_y = pos

        new_pos_x, new_pos_y = pos_x + offset_x, pos_y + offset_y

        if exclude_x == offset_x and exclude_y == offset_y:
            return False
        if not (0 <= new_pos_x < self.m_row and 0 <= new_pos_y < self.n_col):
            return False

        if curr_d_cost[new_pos_x][new_pos_y] <= curr_d_cost[pos_x][pos_y] + cost_cell:
            return False
        curr_d_cost[new_pos_x][new_pos_y] = curr_d_cost[pos_x][pos_y] + cost_cell
        return True


class OceanCurrentsAdapter:
    def __init__(self, raw_inp: str):
        self.raw_inp: str = raw_inp

        self.m_row: int = -1
        self.n_col: int = -1
        self.num_test: int = -1
        self.test_cases: List[dict] = []
        self.mtx: List[List[int]] = []

    def build(self):

        raw_rows = self.raw_inp.split('\n')
        head_inp = raw_rows[0].split(' ')
        self.m_row, self.n_col = int(head_inp[0]), int(head_inp[1])

        for i in range(self.m_row):
            raw_row = raw_rows[i + 1]
            self.mtx.append([int(e) for e in raw_row])

        cur_pos = 1 + self.m_row

        self.num_test = int(raw_rows[cur_pos])

        cur_pos += 1
        for i in range(self.num_test):
            raw_row = raw_rows[cur_pos + i].split(' ')
            s_x, s_y, d_x, d_y = [int(e)-1 for e in raw_row]
            self.test_cases.append({'s': (s_x, s_y), 'd': (d_x, d_y)})

    def to_solution(self) -> List[OceanCurrentsSolution]:

        return [
            OceanCurrentsSolution(self.m_row, self.n_col, self.mtx, self.test_cases[i]['s'], self.test_cases[i]['d'])
            for i in range(self.num_test)]


raw_inp = '''5 5
04125
03355
64734
72377
02062
3
4 2 4 2
4 5 1 4
5 3 3 4'''

adp = OceanCurrentsAdapter(raw_inp)

adp.build()

slns: List[OceanCurrentsSolution] = adp.to_solution()

print(slns[2].bfs_solve())
