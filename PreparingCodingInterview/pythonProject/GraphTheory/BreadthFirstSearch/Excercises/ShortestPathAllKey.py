from typing import List, Tuple, Deque
from collections import deque


def is_starting_point(c: str):
    return c == '@'


def is_key(c: str):
    return c.isalpha() and c.islower()


def is_lock(c: str):
    return c.isalpha() and c.isupper()


def get_key_offset(c: str):
    return ord(c.lower()) - ord('a')


def is_wall(c: str):
    return c == '#'


def is_empty(c: str):
    return c == '.'


def contain_key(key: str, bit_key_arr: int) -> bool:
    key_idx = get_key_offset(key)

    return ((1 << key_idx) & bit_key_arr) != 0


class ShortestPathAllKeySolution:
    def __init__(self, grid: List[str]):
        self.grid: List[str] = grid
        self.m_row: int = len(self.grid)
        self.n_col: int = len(self.grid[0])

    def find_starting_point(self) -> Tuple[int, int]:
        for i in range(self.m_row):
            for j in range(self.n_col):
                if is_starting_point(self.grid[i][j]):
                    return i, j
        return -1, -1

    def count_num_key(self) -> int:
        num_key = 0
        for i in range(self.m_row):
            for j in range(self.n_col):
                if is_key(self.grid[i][j]):
                    num_key += 1
        return num_key

    def solve(self) -> int:

        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        start_point: Tuple[int, int] = self.find_starting_point()

        num_key = self.count_num_key()

        if num_key == 0:
            return 0
        num_comb = 1 << num_key
        visited: List[List[List[bool]]] = [[[False] * self.n_col for _ in range(self.m_row)] for _ in range(num_comb)]

        q: Deque[Tuple[int, int, int, int]] = deque()

        q.append((0, 0, start_point[0], start_point[1]))
        visited[0][start_point[0]][start_point[1]] = True
        while q:
            num_step, bit_key, pos_i, pos_j = q.popleft()

            if bit_key == num_comb - 1:
                return num_step
            for dir_i, dir_j in directions:
                nxt_i, nxt_j = pos_i + dir_i, pos_j + dir_j
                nxt_bit_key = bit_key
                if not (0 <= nxt_i < self.m_row and 0 <= nxt_j < self.n_col):
                    continue
                cell_sign = self.grid[nxt_i][nxt_j]
                if is_wall(cell_sign):
                    continue
                if is_lock(cell_sign) and not contain_key(cell_sign, nxt_bit_key):
                    continue
                if is_key(cell_sign) and not contain_key(cell_sign, nxt_bit_key):
                    nxt_bit_key = (1 << get_key_offset(cell_sign)) | nxt_bit_key

                if visited[nxt_bit_key][nxt_i][nxt_j]:
                    continue
                visited[nxt_bit_key][nxt_i][nxt_j] = True
                q.append((num_step + 1, nxt_bit_key, nxt_i, nxt_j))

        return -1


grid1: List[str] = ["@Aa"]
sln = ShortestPathAllKeySolution(grid1)

print(sln.solve())
