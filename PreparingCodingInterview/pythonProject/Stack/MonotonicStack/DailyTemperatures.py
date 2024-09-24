from typing import List, Tuple, Deque
from collections import deque


class DailyTemperaturesSolution:
    def __init__(self, temperatures: List[int]):
        self.temperatures: List[int] = temperatures

    def solve(self) -> List[int]:

        answers: List[int] = [0] * len(self.temperatures)
        st: Deque[Tuple[int, int]] = deque()
        for i in range(len(self.temperatures) - 1, -1, -1):

            cur_temp = self.temperatures[i]
            while st and st[-1][1] <= cur_temp:
                st.pop()
            if st:
                answers[i] = st[-1][0] - i
            st.append((i, cur_temp))

        return answers


temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]

sln = DailyTemperaturesSolution(temperatures1)

print(sln.solve())
