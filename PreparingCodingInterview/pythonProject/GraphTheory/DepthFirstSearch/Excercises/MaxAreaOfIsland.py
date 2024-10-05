from typing import List, Tuple


class DSU:
    def __init__(self, m_row, n_col):
        self.par: List[List[Tuple[int, int]]] = [[(i, j) for j in range(n_col)] for i in range(m_row)]
        self.area: List[List[int]] = [[1] * n_col for _ in range(m_row)]

    def find_par(self, u_i: int, u_j: int) -> Tuple[int, int]:

        if (u_i, u_j) == self.par[u_i][u_j]:
            return u_i, u_j

        self.par[u_i][u_j] = self.find_par(*self.par[u_i][u_j])

        return self.par[u_i][u_j]

    def join(self, u: Tuple[int, int], v: Tuple[int, int]) -> int:

        par_u_i, par_u_j = self.find_par(*u)
        par_v_i, par_v_j = self.find_par(*v)

        if par_u_i == par_v_i and par_u_j == par_v_j:
            return self.area[par_u_i][par_u_j]

        self.par[par_v_i][par_v_j] = (par_u_i, par_u_j)

        self.area[par_u_i][par_u_j] += self.area[par_v_i][par_v_j]

        return self.area[par_u_i][par_u_j]


class MaxAreaOfIslandSolution:

    def __init__(self, grid: List[List[int]]):
        self.grid: List[List[int]] = grid

    def dfs_solve(self) -> int:

        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m_row, n_col = len(self.grid), len(self.grid[0])

        visited: List[List[int]] = [[False] * n_col for _ in range(m_row)]

        def dfs_count(u_i: int, u_j: int) -> int:

            visited[u_i][u_j] = True

            area_island = 1
            nonlocal m_row, n_col
            for dir_i, dir_j in directions:
                v_i, v_j = u_i + dir_i, u_j + dir_j

                if not (0 <= v_i < m_row and 0 <= v_j < n_col):
                    continue
                if self.grid[v_i][v_j] == 0 or visited[v_i][v_j]:
                    continue

                area_island += dfs_count(v_i, v_j)

            return area_island

        max_area: int = 0

        for i in range(m_row):
            for j in range(n_col):
                if visited[i][j] or self.grid[i][j] == 0:
                    continue
                max_area = max(max_area, dfs_count(i, j))
        return max_area

    def solve_by_union_join(self) -> int:

        max_area = 0
        m_row, n_col = len(self.grid), len(self.grid[0])
        dsu = DSU(m_row, n_col)
        for i in range(m_row):
            for j in range(n_col):
                if self.grid[i][j] == 0:
                    continue
                max_area = max(max_area, 1)
                for dir_i, dir_j in [(0, 1), (1, 0)]:
                    neigh_i, neigh_j = i + dir_i, j + dir_j

                    if neigh_i == m_row or neigh_j == n_col:
                        continue

                    if self.grid[neigh_i][neigh_j] == 0:
                        continue
                    max_area = max(max_area, dsu.join((i, j), (neigh_i, neigh_j)))

        return max_area


grid1 = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

sln = MaxAreaOfIslandSolution(grid1)

print(sln.dfs_solve())
print(sln.solve_by_union_join())
