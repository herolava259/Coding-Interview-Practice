from typing import List, Deque as Stack, DefaultDict as Table
from collections import deque as stack, defaultdict


class NextGreaterElementSolution:
    def __init__(self, nums1: List[int], nums2: List[int]):

        self.nums1: List[int] = nums1
        self.nums2: List[int] = nums2

    def solve(self) -> List[int]:

        inverted_tb: Table[int, int] = defaultdict(lambda : -1)

        for idx, num in enumerate(self.nums1):
            inverted_tb[num] = idx
        st: Stack[int] = stack()

        ans = [-1] * len(self.nums1)
        for num in self.nums2[::-1]:

            while st and st[-1] <= num:
                st.pop()

            if st and inverted_tb[num] != -1:
                ans[inverted_tb[num]] = st[-1]

            st.append(num)

        return ans

nums1 = [2,4]
nums2 = [1,2,3,4]

print(NextGreaterElementSolution(nums1, nums2).solve())


