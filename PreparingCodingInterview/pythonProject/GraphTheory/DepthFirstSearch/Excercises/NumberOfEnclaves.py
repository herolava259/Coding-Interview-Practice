from typing import List, Tuple


class NumEnclavesSolution:
    def __init__(self, grid: List[List[int]]):

        self.grid: List[List[int]] = grid

    def solve(self) -> int:
        m_row, n_col = len(self.grid), len(self.grid[0])
        visited: List[List[bool]] = [[False] * n_col for _ in range(m_row)]
        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs_find(u_i: int, u_j: int) -> Tuple[bool, int]:
            nonlocal m_row, n_col

            num_cell = 1
            water_around: bool = True
            if u_i == 0 or u_i == m_row - 1 or u_j == 0 or u_j == n_col - 1:
                water_around = False

            for dir_row, dir_col in directions:
                v_i, v_j = u_i + dir_row, u_j + dir_col
                if not (0 <= v_i < m_row and 0 <= v_j < n_col):
                    continue
                if visited[v_i][v_j] or self.grid[v_i][v_j] == 0:
                    continue
                visited[v_i][v_j] = True
                check, child_cell = dfs_find(v_i, v_j)
                if not check:
                    water_around = False
                num_cell += child_cell

            return water_around, num_cell

        num_cells = 0

        for i in range(m_row):
            for j in range(n_col):
                if visited[i][j] or self.grid[i][j] == 0:
                    continue

                visited[i][j] = True
                c_check, n_cell = dfs_find(i, j)

                if c_check:
                    num_cells += n_cell

        return num_cells


grid1 = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]

sln = NumEnclavesSolution(grid1)

print(sln.solve())