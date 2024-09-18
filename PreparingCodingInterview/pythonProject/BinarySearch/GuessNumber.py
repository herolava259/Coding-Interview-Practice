import random
from typing import List


def guess(num: int) -> int:
    pick_number = random.randint(1, 1000)

    if num == pick_number:
        return 0
    if num < pick_number:
        return 1
    if num > pick_number:
        return -1


class GuessNumberSolution:
    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> int:

        first, last = 1, self.n

        while first < last:
            mid = (first + last) // 2
            result = guess(mid)

            if result == 1:
                first = mid + 1
            elif result == -1:
                last = mid - 1
            elif result == 0:
                return mid

        return first
