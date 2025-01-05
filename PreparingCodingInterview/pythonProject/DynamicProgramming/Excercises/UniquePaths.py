from typing import List


class UniquePathsSolution:
    def __init__(self, m: int, n: int):
        self.m: int = m
        self.n: int = n

    def solve(self) -> int:

        prev_row = [1] * self.n
        cur_row = [0] * self.n
        cur_row[0] = 1
        for _ in range(1, self.m):

            for i in range(1, self.n):
                cur_row[i] = cur_row[i - 1] + prev_row[i]

            prev_row, cur_row = cur_row, prev_row

        return prev_row[-1]


sln = UniquePathsSolution(3, 7)

print(sln.solve())
