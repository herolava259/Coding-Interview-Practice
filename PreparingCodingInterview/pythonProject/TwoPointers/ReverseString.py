from typing import List


class ReverseStringSolution:
    def __init__(self, s: List[str]):
        self.s = s

    def solve(self) -> None:

        p_left, p_right = 0, len(self.s)-1

        while p_left < p_right:
            self.s[p_left], self.s[p_right] = self.s[p_right], self.s[p_left]

            p_left += 1
            p_right -= 1
