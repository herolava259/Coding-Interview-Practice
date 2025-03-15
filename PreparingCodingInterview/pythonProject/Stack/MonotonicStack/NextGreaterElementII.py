from typing import List, Deque as Stack
from collections import deque as stack


class NextGreaterElementIISolution:
    def __init__(self, nums: List[int]):

        self.nums: List[int] = nums

    def solve(self) -> List[int]:
        n = len(self.nums)

        ans: List[int] = [-1] * n

        st: Stack[int] = stack()

        for i in range(2 * n - 2, -1, -1):

            idx = i % n
            num = self.nums[idx]
            while st and st[-1] <= num:
                st.pop()
            if st and i < n:
                ans[i] = st[-1]
            st.append(num)

        return ans

nums1 = [2]
print(NextGreaterElementIISolution(nums1).solve())
