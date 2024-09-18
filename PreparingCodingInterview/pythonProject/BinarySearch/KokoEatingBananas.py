import math
from typing import List


class MinEatingSpeedSolution:

    def __init__(self, piles: List[int], h: int):

        self.piles: List[int] = piles
        self.h: int = h

    def solve(self) -> int:

        f_speed = 1
        l_speed = 10 ** 4

        while f_speed < l_speed:
            mid_speed = (f_speed + l_speed) >> 1

            cur_h = self.calc_hours(mid_speed)

            if cur_h <= self.h:
                l_speed = mid_speed - 1
            else:
                f_speed = mid_speed + 1

        if self.calc_hours(f_speed) > self.h:
            f_speed += 1

        return f_speed

    def calc_hours(self, speed: int):

        total_h = 0
        for p in self.piles:
            total_h += math.ceil(p / speed)

        return total_h


piles1 = [3, 6, 7, 11]
h1 = 8

sln = MinEatingSpeedSolution(piles1, h1)

print(sln.solve())
