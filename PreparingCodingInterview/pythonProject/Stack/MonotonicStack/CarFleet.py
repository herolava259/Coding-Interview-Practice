from typing import List, Deque as Stack
from collections import deque as stack

class CarFleetSolution:
    def __init__(self, target: int, position: List[int], speed: List[int]):
        self.target: int = target
        self.position: List[int] = position
        self.speed: List[int] = speed

    def solve(self) -> int:

        n = len(self.position)

        car = sorted(zip(self.position, self.speed), key= lambda c: c[0])

        time: List[float] = [float(self.target - pos) / ve for pos, ve in car]

        st: Stack[float] = stack()

        st.append(time[0])

        for i in range(1, n):

            while st and st[-1] <= time[i]:
                st.pop()
            st.append(time[i])

        return len(st)

print(CarFleetSolution(100, [0, 2, 4], [4, 2, 1]).solve())


