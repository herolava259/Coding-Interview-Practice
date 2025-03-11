from typing import List, Deque as Stack
from collections import deque as stack


class RemoveKDigitsSolution:
    def __init__(self, num: str, k: int):
        self.num: str = num
        self.k: int = k

    def solve(self) -> str:

        st: Stack[str] = stack()
        n = len(self.num)

        p = 0
        counter = 0
        while p < n:
            digit = self.num[p]
            while counter < self.k and st and st[-1] > digit:
                st.pop()
                counter += 1
            if st or digit != '0':
                st.append(digit)
            p += 1

        while counter < self.k:
            st.pop()
            counter += 1

        return ''.join(st) or '0'

num1 = "1234567890"
k1 = 9

print(RemoveKDigitsSolution(num1, k1).solve())