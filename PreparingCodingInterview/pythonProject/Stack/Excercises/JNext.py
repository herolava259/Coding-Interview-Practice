from typing import List
from collections import deque


class JustNextSolution:

    def __init__(self, digits: List[int]):
        self.digits: List[int] = digits

    def solve(self) -> List[int] | None:

        s: deque= deque()

        n = len(self.digits)

        idx = n -2

        while idx >= 0 and self.digits[idx] >= self.digits[idx+1]:
            idx -= 1
        if idx < 0:
            return None
        tmp = 0
        for i in range(idx+1, n):
            if self.digits[idx] >= self.digits[i]:
                tmp, self.digits[i-1] = self.digits[i-1], self.digits[idx]
            s.append(self.digits[i])
        self.digits[idx] = tmp
        idx += 1
        while idx < n:
            self.digits[idx] = s.pop()
            idx += 1
        return self.digits