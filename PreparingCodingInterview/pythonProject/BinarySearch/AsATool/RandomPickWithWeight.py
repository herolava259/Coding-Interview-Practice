import random
from typing import List


class RandomPickSolution:
    def __init__(self, w: List[int]):
        self.w :List[int] = w
        self.n: int = len(self.w)
        self.pdf_w: List[float] = [0.0] * self.n
        sum_w: float = float(sum(w))
        acum_w: int = self.w[0]
        self.pdf_w[0] = acum_w / sum_w
        for i in range(1, self.n):
            acum_w += self.w[i]
            self.pdf_w = acum_w / sum_w

    def pick_index(self) -> int:

        rnd = random.random()

        low, high = 0, self.n-1

        while low < high:
            mid = (low+high) >> 1

            if self.pdf_w[mid] < rnd:
                low = mid + 1
            else:
                high = mid
        return low

