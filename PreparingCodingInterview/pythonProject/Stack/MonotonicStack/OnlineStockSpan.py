from typing import Deque, Tuple
from collections import deque


class StockSpanner:

    def __init__(self):
        self.st: Deque[Tuple[int, int]] = deque()
        self.counter: int = 1

    def next(self, price: int) -> int:

        while self.st and self.st[-1][1] <= price:
            prev_day, _ = self.st.pop()

        if self.st:
            span = self.counter - self.st[-1][0]
        else:
            span = self.counter

        self.st.append((self.counter, price))
        self.counter += 1

        return span


test1 = [100, 80, 60, 70, 60, 75, 85]

spanner = StockSpanner()

for t in test1:
    print(spanner.next(t))
