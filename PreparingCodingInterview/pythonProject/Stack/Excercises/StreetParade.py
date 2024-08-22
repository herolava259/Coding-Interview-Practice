from typing import List
from collections import deque

class StreetParadeSolution:
    def __init__(self, trucks: List[int]):

        self.trucks: List[int] = trucks

    def solve(self) -> bool:

        s_dest: deque = deque()
        s_temp: deque = deque()

        s_src = list(self.trucks)
        correct_truck = 1
        n = len(self.trucks)
        while correct_truck <= n:
            if s_temp and s_temp[-1] == correct_truck:
                s_temp.pop()
                s_dest.append(correct_truck)
                correct_truck += 1
                continue

            while s_src and s_src[-1] != correct_truck:
                s_temp.append(s_src[-1])

            if not s_src:
                return False
            s_dest.append(s_src.pop())
            correct_truck += 1
                
        return True