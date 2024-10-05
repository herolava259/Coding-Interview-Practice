from typing import List, Tuple, Set


class DSU:
    def __init__(self, m_row: int, n_col):

        self.m_row: int = m_row
        self.n_col: int = n_col

        self.par: List[List[Tuple[int, int]]] = [[(i, j) for j in range(n_col)] for i in range(m_row)]
        self.state: List[List[bool]] = [
            [True if i in (0, m_row - 1) or j in (0, n_col - 1) else False for j in range(n_col)]
            for i in range(m_row)]

    def find_par(self, u_i: int, u_j: int) -> Tuple[int, int]:

        if self.par[u_i][u_j] == (u_i, u_j):
            return u_i, u_j
        self.par[u_i][u_j] = self.find_par(*self.par[u_i][u_j])

        return self.par[u_i][u_j]

    def join(self, u: Tuple[int, int], v: Tuple[int, int]) -> Tuple[int, int]:

        par_u_i, par_u_j = self.find_par(*u)
        par_v_i, par_v_j = self.find_par(*v)

        if par_u_i == par_v_i and par_u_j == par_v_j:
            if self.state[u[0]][u[1]] or self.state[u[0]][u[1]]:
                self.state[par_u_i][par_u_j] = True
            return par_u_i, par_u_j

        self.par[par_v_i][par_v_j] = (par_u_i, par_u_j)

        self.state[par_u_i][par_u_j] = self.state[par_u_i][par_u_j] or self.state[par_v_i][par_v_j] or self.state[u[0]][u[1]] \
                                       or self.state[v[0]][v[1]]
        return par_u_i, par_u_j


class NumberOfClosedIslandSolution:
    def __init__(self, grid: List[List[int]]):

        self.grid: List[List[int]] = grid

    def solve(self) -> int:

        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m_row, n_col = len(self.grid), len(self.grid[0])

        visited: List[List[bool]] = [[False] * n_col for _ in range(m_row)]

        def dfs_find(u_i: int, u_j: int) -> bool:

            nonlocal m_row, n_col
            near_bound: bool = False
            visited[u_i][u_j] = True
            if u_i == 0 or u_i == m_row - 1 or u_j == 0 or u_j == n_col - 1:
                near_bound = True

            for dir_i, dir_j in directions:
                v_i, v_j = u_i + dir_i, u_j + dir_j

                if not (0 <= v_i < m_row and 0 <= v_j < n_col):
                    continue
                if visited[v_i][v_j] or self.grid[v_i][v_j] == 1:
                    continue

                near_bound |= dfs_find(v_i, v_j)

            return near_bound

        num_island = 0
        for i in range(m_row):
            for j in range(n_col):
                if visited[i][j] or self.grid[i][j] == 1:
                    continue
                if i == 1 and j == 1:
                    pass
                neared_bound = dfs_find(i, j)
                if not neared_bound:
                    num_island += 1

        return num_island

    def solve_by_union_find(self) -> int:

        m_row, n_col = len(self.grid), len(self.grid[0])

        dsu = DSU(m_row, n_col)

        node_set: Set[Tuple[int, int]] = set()

        for i in range(m_row):
            for j in range(n_col):
                if self.grid[i][j] == 1:
                    continue
                check = True
                for dir_i, dir_j in [(0, 1), (1, 0)]:
                    near_i, near_j = i + dir_i, j + dir_j
                    if near_i >= m_row or near_j >= n_col:
                        continue
                    if self.grid[near_i][near_j] == 1:
                        continue

                    check = False
                    node_set.add(dsu.join((i, j), (near_i, near_j)))
                if check:
                    node_set.add((i, j))
        num_island = 0
        prev_nodes: Set[Tuple[int, int]] = set()
        for u_i, u_j in node_set:
            par_u_i, par_u_j = dsu.find_par(u_i, u_j)
            if (par_u_i, par_u_j) not in prev_nodes and not dsu.state[par_u_i][par_u_j]:
                num_island += 1
            prev_nodes.add((par_u_i, par_u_j))
        return num_island


grid1 =[[0,1,1,1,0],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0]]

sln = NumberOfClosedIslandSolution(grid1)

print(sln.solve())
print(sln.solve_by_union_find())
