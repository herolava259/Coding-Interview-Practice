from typing import List, Tuple, Deque
from collections import deque

class CutDownSolution:
    def __init__(self, h: List[int]):
        self.h: List[int] = h

    def solve(self) -> Tuple[int, List[int]]:

        def calc_reach_out_left(arr: List[int]) -> List[int]:

            st: Deque[int] = deque()
            l: List[int] = [0] * (len(self.h) + 1)
            for i in range(1, len(arr) + 1):
                l[i] = i
                while st and st[-1] > i-arr[i]:
                    l[i] = min(l[i], l[st.pop()])

                st.append(i)
            return l

        def calc_reach_out_right(arr: List[int]) -> List[int]:

            st: Deque[int] = deque()

            r: List[int] = [i_t for i_t in range(len(arr) + 1)]

            for i in range(len(arr), 0, -1):

                while st and st[-1] < i + arr[i]:
                    r[i] = min(r[i], r[st.pop()])

                st.append(i)

            return r

        reach_left: List[int] = calc_reach_out_left(self.h)
        reach_right: List[int] = calc_reach_out_right(self.h)

        trace: List[int] = [-j for j in range(len(self.h) + 1)]
        s: Deque[int] = deque()

        dp: List[int] = [0] * (len(self.h) + 1)

        for j in range(1, len(self.h)+1):

            if dp[j] > dp[reach_left[j] - 1] + 1:
                dp[j] = dp[reach_left[j] - 1] + 1
                trace[j] = -reach_left[j]

            while s and reach_right[s[-1]] < j:
                s.pop()

            if s and dp[j] > dp[s[-1]-1] + 1:
                dp[j] = dp[s[-1]-1] + 1
                trace[j] = s[-1]

            if s or dp[s[-1] - 1] > dp[j-1]:
                s.append(j)

        return dp[-1], trace



