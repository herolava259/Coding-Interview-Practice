from typing import List, Deque as Stack
from collections import deque as stack


class LongestWellPerformingIntervalSolution:
    def __init__(self, hours: List[int]):

        self.hours: List[int] = hours

    def solve(self) -> int:

        n = len(self.hours) + 1
        streaks: List[int] = [0] * n


        for i in range(1, n):
            streaks[i] = streaks[i-1]
            if self.hours[i-1] > 8:
                streaks[i] += 1
            else:
                streaks[i] -= 1

        dec_st: Stack[int] = stack()

        for i in range(n):

            if not dec_st or streaks[dec_st[-1]] > streaks[i]:
                dec_st.append(i)

        peak = -10**9-7
        max_interval = 0
        for i in range(n-1, -1, -1):
            if streaks[i] <= peak:
                continue
            if not dec_st:
                break
            while dec_st and i <= dec_st[-1]:
                dec_st.pop()

            peak = streaks[i]
            while dec_st and streaks[dec_st[-1]] < peak:
                beg = dec_st.pop()
                max_interval = max(max_interval, i - beg)

        return max_interval

hours1 = [6,6,9]

print(LongestWellPerformingIntervalSolution(hours1).solve())