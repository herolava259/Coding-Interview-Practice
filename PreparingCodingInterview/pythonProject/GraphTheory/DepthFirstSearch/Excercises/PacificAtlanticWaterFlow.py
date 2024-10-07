from typing import List, Tuple, Set


# 417

class PacificAtlanticSolution:
    def __init__(self, heights: List[List[int]]):
        self.heights: List[List[int]] = heights

    def solve(self) -> List[List[int]]:
        m_row, n_col = len(self.heights), len(self.heights[0])

        directions: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        result: List[List[int]] = []

        def dfs_reach_ocean(pos_i: int, pos_j: int, positions: Set[Tuple[int, int]], prev_h: int = 100001) \
                -> Tuple[bool, bool]:

            cur_h = self.heights[pos_i][pos_j]
            if cur_h > prev_h:
                return False, False
            positions.add((pos_i, pos_j))
            nonlocal m_row, n_col
            reach_pacific = False
            reach_atlantic = False

            if pos_i == 0 or pos_j == 0:
                reach_pacific = True
            if pos_i == m_row - 1 or pos_j == n_col - 1:
                reach_atlantic = True

            for dir_i, dir_j in directions:

                if reach_pacific and reach_atlantic:
                    return True, True

                near_i, near_j = pos_i + dir_i, pos_j + dir_j

                if (near_i, near_j) in positions:
                    continue
                if not (0 <= near_i < m_row and 0 <= near_j < n_col):
                    continue
                near_pacific, near_atlantic = dfs_reach_ocean(near_i, near_j, positions, cur_h)

                if near_pacific:
                    reach_pacific = True
                if near_atlantic:
                    reach_atlantic = True

            return reach_pacific, reach_atlantic

        for i in range(m_row):
            for j in range(n_col):
                if (i, j) == (1, 8):
                    pass
                if dfs_reach_ocean(i, j, set()) == (True, True):
                    result.append([i, j])

        return result


heights1 = [[12,7,7,14,6,17,12,17,8,18,9,5],
            [6,8,12,5,3,6,2,14,19,6,18,13],
            [0,6,3,8,8,10,8,17,13,13,13,12],
            [5,6,8,8,15,16,19,14,7,11,2,3],
            [7,18,2,7,10,10,3,14,13,15,15,7],
            [18,6,19,4,12,3,3,2,6,6,19,6],
            [3,18,5,16,19,6,3,12,6,0,14,11],
            [9,10,17,12,10,11,11,9,0,0,12,0],
            [4,13,3,0,4,12,9,5,6,17,10,11],
            [18,3,5,0,8,19,18,4,8,19,1,3],
            [16,2,14,6,4,14,7,2,9,7,13,18],
            [0,16,19,16,16,4,15,19,7,0,3,16],
            [13,8,12,8,2,3,5,18,6,15,18,6],
            [4,10,8,1,16,0,6,0,14,10,11,8],
            [7,1,3,4,11,12,9,0,6,2,17,5],
            [1,16,6,1,0,19,11,1,5,7,8,2],
            [4,1,14,13,14,7,3,7,1,9,15,18],
            [14,11,6,14,14,14,4,0,11,17,1,9],
            [3,14,2,10,3,1,9,16,1,13,0,15],
            [8,9,13,5,5,7,10,1,4,5,0,9],
            [13,16,15,5,17,6,16,13,5,7,3,15],
            [5,1,12,19,3,13,0,0,3,10,6,13],
            [12,17,9,16,16,6,2,6,12,15,14,16],
            [7,7,0,6,4,15,1,7,17,5,2,12],
            [3,17,0,2,4,5,11,7,16,16,16,13],
            [3,7,16,11,2,16,14,9,16,17,10,3],
            [12,18,17,17,5,15,1,2,12,12,5,7],
            [11,10,10,0,11,7,17,14,5,15,2,16],
            [7,19,14,7,6,2,4,16,11,19,14,14],
            [6,17,6,6,6,15,9,12,8,13,1,7],
            [16,3,15,0,18,17,0,11,3,16,11,12],
            [15,12,4,6,19,15,17,7,3,9,2,11]]

sln = PacificAtlanticSolution(heights1)

print(sln.solve())
