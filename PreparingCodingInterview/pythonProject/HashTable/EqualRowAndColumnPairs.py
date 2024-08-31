from typing import List


class EqualRowAndColumnSolution:
    def __init__(self, grid: List[List[int]]):
        self.grid: List[List[int]] = grid

    def solve(self) -> int:

        count_pair = 0
        map_table = dict()

        for row in self.grid:
            row_tuple = tuple(row)
            map_table[row_tuple] = map_table.get(row_tuple, 0) + 1

        for col in zip(*self.grid):
            col_tuple = tuple(col)
            count_pair += map_table.get(col_tuple, 0)

        return count_pair

grid1 = [[3,2,1],[1,7,6],[2,7,7]]

sln = EqualRowAndColumnSolution(grid1)

print(sln.solve())