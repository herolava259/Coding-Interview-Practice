from typing import List


class SearchMatrixSolution:
    def __init__(self, mtx: List[List[int]], target: int):

        self.mtx: List[List[int]] = mtx

        self.target: int = target

    def solve(self) -> bool:

        m, n = len(self.mtx), len(self.mtx[0])

        def binary_2D_search(first_i: int, last_i: int, first_j: int, last_j: int) -> bool:

            if first_i == last_i and first_j == last_j:
                return self.mtx[first_i][first_j] == self.target

            mid_i, mid_j = (first_i + last_i) // 2, (first_j + last_j) // 2

            if self.mtx[mid_i][mid_j] == self.target:
                return True

            if self.mtx[mid_i][mid_j] < self.target:
                return binary_2D_search(min(mid_i + 1, last_i), last_i, first_j, mid_j) \
                       or binary_2D_search(first_i, mid_i, min(mid_j + 1, last_j), last_j) \
                       or binary_2D_search(min(mid_i + 1, last_i), last_i, min(mid_j + 1, last_j), last_j)

            return binary_2D_search(first_i, mid_i, first_j, mid_j) \
                   or binary_2D_search(min(mid_i + 1, last_i), last_i, first_j, mid_j) \
                   or binary_2D_search(first_i, mid_i, min(mid_j + 1, last_j), last_j)

        return binary_2D_search(0, m - 1, 0, n - 1)


matrix1 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
target1 = 5

sln = SearchMatrixSolution(matrix1, target1)

print(sln.solve())
