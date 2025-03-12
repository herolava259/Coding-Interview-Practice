from typing import List, Deque as Stack
from collections import deque as stack

class Find132PatternSolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> bool:

        st_dec: Stack[int] = stack()

        min_s: int = self.nums[0]
        min_until: List[int] = [self.nums[0]] * len(self.nums)
        for idx in range(len(self.nums)):

            while st_dec and self.nums[st_dec[-1]] <= self.nums[idx]:
                st_dec.pop()

            if st_dec and min_until[st_dec[-1]] < self.nums[idx]:
                return True

            min_s = min(self.nums[idx], min_s)
            min_until[idx] = min_s

            if min_until[idx] != self.nums[idx]:
                st_dec.append(idx)


        return False

nums1 = [1,0,1,-4,-3]

print(Find132PatternSolution(nums1).solve())
