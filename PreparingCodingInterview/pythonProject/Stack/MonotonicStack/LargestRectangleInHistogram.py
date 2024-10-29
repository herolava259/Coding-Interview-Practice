from typing import List, Deque
from collections import deque


class LargestRectangleAreaSolution:
    def __init__(self, heights: List[int]):
        self.heights: List[int] = heights

    def solve(self) -> int:
        n = len(self.heights)
        pair_idxs = zip(calc_furthest_stick(self.heights, n), reversed(calc_furthest_stick(self.heights[::-1], n)))

        max_area = 0

        for idx, w_range in enumerate(pair_idxs):
            beg_w, end_w = w_range
            end_w = n - 1 - end_w
            max_area = max(max_area, (end_w - beg_w+1) * self.heights[idx])
        return max_area


def calc_furthest_stick(heights: List[int], n: int) -> List[int]:
    st: Deque[int] = deque()
    indexes: List[int] = [0] * n
    for i in range(n):

        cur_h = heights[i]
        end_i = i
        while st and heights[st[-1]] >= cur_h:
            end_i = st.pop()

        cur_p = -1

        if st:
            cur_p = st[-1]

        while cur_p+1 < end_i and heights[cur_p + 1] < cur_h:
            cur_p += 1
        st.append(i)
        indexes[i] = cur_p + 1

    return indexes


heights1 = [2, 1, 2]

sln = LargestRectangleAreaSolution(heights1)

print(sln.solve())
