from typing import List


class HighestAltitudeSolution:

    def __init__(self, gain: List[int]):
        self.gain: List[int] = gain

    def solve(self) -> int:
        max_h = 0

        cur_altitude = 0

        for g in self.gain:
            cur_altitude += g
            max_h = max(cur_altitude, max_h)

        return max_h


gain1 = [-5, 1, 5, 0, -7]

sln = HighestAltitudeSolution(gain1)

print(sln.solve())
