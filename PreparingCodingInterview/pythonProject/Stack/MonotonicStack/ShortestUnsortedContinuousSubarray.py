from typing import List, Deque as Stack
from collections import deque as stack

class FindUnsortedSubarraySolution:
    def __init__(self, nums: List[int]):
        self.nums: List[int] = nums

    def solve(self) -> int:

        n = len(self.nums)

        st: Stack[int] = stack()
        # st.extend(range(beg+1))
        st.append(0)
        for i in range(1,n):
            while st and self.nums[st[-1]] > self.nums[i]:
                st.pop()

            if not st:
                break
            st.append(i)
        beg = -1
        while st and st[0] == beg+1:
            beg = st.popleft()

        if beg == n-1:
            return 0
        st.clear()
        st.append(n-1)

        for i in range(n-2, -1, -1):
            while st and self.nums[i] > self.nums[st[-1]]:
                st.pop()
            if not st:
                break
            st.append(i)
        end = n
        while st and end == st[0] + 1:
            end = st.popleft()

        return max(0, end - beg - 1)


nums1 = [2,6,4,8,10,9,15]

print(FindUnsortedSubarraySolution(nums1).solve())
