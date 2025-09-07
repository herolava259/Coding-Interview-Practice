from typing import List, Tuple

def fenwick_loop(u: int, v: int, asc: bool = True):
    p = u if asc else v

    if asc:
        while p <= v:
            yield p
            p += p & (-p)
    else:
        while p >= u:
            yield p
            p -= p & (-p)

class FenwickTree2DimForRectSum:
    def __init__(self, mtx: List[List[int]]):

        self.mtx: List[List[int]] = mtx
        self.m_row: int = len(self.mtx)
        self.n_col: int = len(self.mtx[0])
        self.bit_mtx: List[List[int]] = [[0] * self.n_col for _ in range(self.m_row)]
        self.bit_volume: List[List[List[int]]] = [[[0] * self.n_col for _ in range(self.m_row)] for _ in range(4)]

    def add_value(self, u_row: int, v_col: int, x_val: int):
        for p_row in fenwick_loop(u_row, self.m_row):
            for p_col in fenwick_loop(v_col, self.n_col):
                self.bit_mtx[p_row][p_col] += x_val

    def initialize(self):
        for i in range(self.m_row):
            for j in range(self.n_col):
                self.add_value(i, j, self.mtx[i][j])
                self.add_rect_all((i, j),(i, j) ,self.mtx[i][j])

    def query_sum_rect(self, u_row: int, v_col: int) -> int:
        sum_reg = 0

        for p_row in fenwick_loop(1, u_row, asc=False):
            for p_col in fenwick_loop(1, v_col, asc=False):
                sum_reg += self.bit_mtx[p_row][p_col]

        return sum_reg

    def add_rect(self, min_point: Tuple[int, int], extreme_point: Tuple[int, int], x_val: int):

        min_row, min_col = min_point
        extreme_row, extreme_col = extreme_point
        self.add_value(min_row, min_col, x_val)
        self.add_value(extreme_row+1, extreme_col+1, x_val)
        self.add_value(extreme_row+1, min_col, -x_val)
        self.add_value(min_row, extreme_col+1, -x_val)

    def add_value_all(self, u_row: int, v_col: int, x_val: int):

        for p_row in fenwick_loop(u_row, self.m_row):
            for p_col in fenwick_loop(v_col, self.n_col):
                self.bit_volume[0][p_row][p_col] += x_val
                self.bit_volume[1][p_row][p_col] += u_row * x_val
                self.bit_volume[2][p_row][p_col] += v_col * x_val
                self.bit_volume[3][p_row][p_col] += u_row * v_col * x_val

    def add_rect_all(self, low_diag_point: Tuple[int, int],
                            high_diag_point: Tuple[int, int],
                            x_val: int):
        low_row, low_col = low_diag_point
        high_row, high_col = high_diag_point

        self.add_value_all(low_row, low_col, x_val)
        self.add_value_all(low_row, high_col + 1, -x_val)
        self.add_value_all(high_row + 1, low_col, -x_val)
        self.add_value_all(high_row + 1, high_col + 1, x_val)

    def query_sum_with_volume(self, u_row: int, v_col: int):

        res: List[int] = [0] * 4

        for ty in range(4):
            for p_row in fenwick_loop(1, u_row, asc=False):
                for p_col in fenwick_loop(1, v_col, asc=False):
                    res[ty] += self.bit_volume[ty][p_row][p_col]

        return res[0] * (u_row+1)*(v_col+1) - res[1] * (v_col + 1) - res[2] * (u_row +1) + res[3]



