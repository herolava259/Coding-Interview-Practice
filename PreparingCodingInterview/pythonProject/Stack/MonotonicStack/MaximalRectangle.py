from typing import List, Deque as Stack
from collections import deque as stack

class MaximalRectangleSolution:
    def __init__(self, matrix: List[List[str]]):
        self.matrix: List[List[str]] = matrix

    def solve(self) -> int:
        m_row, n_col = len(self.matrix), len(self.matrix[0])

        def calc_histogram() -> List[List[int]]:
            nonlocal m_row, n_col
            h = [[0] * n_col for _ in range(m_row)]

            for idx in range(m_row):
                for jdx in range(n_col):
                    h[idx][jdx] = 1 if self.matrix[idx][jdx] == '1' else 0

                    if idx == 0 or h[idx][jdx] == 0:
                        continue
                    h[idx][jdx] += h[idx-1][jdx]

            return h

        hist: List[List[int]] = calc_histogram()

        max_area = 0

        for i in range(m_row):

            boundaries = zip(calc_boundary_hist(hist[i], n_col), reversed(calc_boundary_hist(hist[i][::-1], n_col)))

            for j, boundary in enumerate(boundaries):
                beg_w, end_w = boundary
                width = n_col - end_w - beg_w
                height = hist[i][j]

                max_area = max(max_area, width*height)

        return max_area

def calc_boundary_hist(heights: List[int], n: int) -> List[int]:
    st: Stack[int] = stack()
    indexes: List[int] = [0] * n
    for i in range(n):

        cur_h = heights[i]
        while st and heights[st[-1]] >= cur_h:
            st.pop()

        cur_p = -1

        if st:
            cur_p = st[-1]

        st.append(i)
        indexes[i] = cur_p+1

    return indexes

matrix1 =[["0","0","0","0","0","0","0","1"],
          ["0","0","0","0","0","0","0","1"],
          ["0","0","0","0","0","0","0","1"],
          ["0","0","0","0","0","0","0","1"],
          ["0","0","0","0","0","0","0","1"],
          ["0","0","0","0","0","1","1","1"],
          ["0","0","0","0","0","1","1","1"],
          ["1","1","1","1","1","1","1","1"]]

print(MaximalRectangleSolution(matrix1).solve())