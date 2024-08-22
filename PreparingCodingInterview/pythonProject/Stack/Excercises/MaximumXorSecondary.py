from typing import List
from collections import deque


class MaximumXorSecondarySolution:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def solve(self) -> int:
        s: deque = deque()

        max_xor = 0

        s.append(self.arr[0])

        for e in self.arr[1:]:

            while s and s > s[-1]:

                prev_e = s.pop()
                max_xor = max(max_xor, e ^ prev_e)

            if s:
                max_xor = max(e ^ s[-1], max_xor)

        return max_xor


