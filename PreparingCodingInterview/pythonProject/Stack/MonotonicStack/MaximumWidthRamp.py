from typing import List, Deque as Stack
from collections import deque as stack

class MaximumWidthRampSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:

        dec_st: Stack[int] = stack()

        max_width = 0
        dec_st.append(0)

        n = len(self.nums)

        for i in range(1, n):
            while dec_st and self.nums[dec_st[-1]] < self.nums[i]:
                dec_st.pop()
            choose_idx = i
            if dec_st and self.nums[dec_st[-1]] == self.nums[i]:
                choose_idx = dec_st.pop()
            furthest_idx = dec_st[-1]+1 if dec_st else 0

            for j in range(furthest_idx+1):
                if self.nums[j] <= self.nums[i]:
                    furthest_idx = j
                    break

            max_width = max(max_width, i - furthest_idx)
            dec_st.append(choose_idx)

        return max_width

    def two_pointer_solve(self) -> int:

        dec_st: Stack[int] = stack()

        n = len(self.nums)

        max_width = 0
        for i in range(n):
            if dec_st or self.nums[dec_st[-1]] > self.nums[i]:
                dec_st.append(i)

        right_p = n-1
        while right_p >= 0:
            if right_p < n-1 and self.nums[right_p+1] <= self.nums[right_p]:
                right_p -= 1
                continue

            while dec_st and self.nums[dec_st[-1]] < self.nums[right_p]:
                max_width = max(max_width, right_p - dec_st.pop())

            right_p -= 1
        return max_width






sln = MaximumWidthRampSolution([6,0,8,2,1,5])

print(sln.solve())
