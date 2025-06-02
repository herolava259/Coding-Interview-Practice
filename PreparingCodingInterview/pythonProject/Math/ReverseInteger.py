from typing import List


class ReverseIntegerSolution:
    def __init__(self, x: int):
        self.x = x

    def solve(self) -> int:

        digits: List[int] = []

        x = self.x

        max_val = (1<<32) -1
        min_val = -max_val-1

        negative = False
        if x < 0:
            negative = True
            x = -x

        while x > 0:
            digits.append(x % 10)
            x = x // 10

        reversed_digits = reversed(digits)
        reversed_x = 0
        for i, digit in enumerate(reversed_digits):
            reversed_x += digit * (10 ** i)

            if negative and -reversed_x < min_val:
                return 0
            if not negative and reversed_x > max_val:
                return 0

        if negative:
            reversed_x *= -1

        return reversed_x

x1 = 1563847412

print(ReverseIntegerSolution(x1).solve())


