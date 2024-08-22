from typing import List, Deque
from collections import deque


class TrappingRainWaterSolution:

    def __init__(self, heights: List[int]):
        self.heights: List[int] = heights

    def stack_solve(self) -> int:

        s: Deque[tuple] = deque()

        water = 0

        s.append((0, self.heights[0]))

        n = len(self.heights)

        for i in range(1, n):

            cur_h = self.heights[i]
            less_h = 0
            while s and s[-1][1] <= cur_h:
                prev_idx, prev_h = s.pop()
                water += (i - prev_idx - 1) * (prev_h - less_h)
                less_h = prev_h

            if s:
                prev_idx, prev_h = s[-1]

                water += (i - prev_idx - 1) * (cur_h - less_h)

            s.append((i, cur_h))

        return water

    def two_pointer_solve(self) -> int:

        n = len(self.heights)
        left, right = 0, n - 1

        water = 0

        min_h = min(self.heights[left], self.heights[right])
        max_h = max(self.heights[left], self.heights[right])
        prev_range = right-left-1
        while left < right:

            if self.heights[left] <= self.heights[right]:
                left += 1
                if self.heights[left] > max_h:
                    water += (max_h - min_h) * prev_range
                    min_h = max_h
                    max_h = self.heights[left]
                    prev_range = right - left - 1

            else:
                right -= 1
                if self.heights[right] > max_h:
                    water += (max_h - min_h) * prev_range
                    min_h = max_h
                    max_h = self.heights[right]
                    prev_range = right - left - 1
        return water


heights1 = [4, 2, 0, 3, 2, 5]

sln = TrappingRainWaterSolution(heights=heights1)

print(sln.two_pointer_solve())
