from typing import List


class MinFlipsSolution:

    def __init__(self, a: int, b: int, c: int):
        self.a: int = a
        self.b: int = b
        self.c: int = c

    def solve(self) -> int:

        num_flip = 0

        for i in range(32):

            cur_bit_a = (self.a >> i) & 1
            cur_bit_b = (self.b >> i) & 1
            cur_bit_c = (self.c >> i) & 1

            if ((cur_bit_a | cur_bit_b) ^ cur_bit_c) == 0:
                continue

            if cur_bit_c == 0:
                if cur_bit_a == 1:
                    num_flip += 1
                if cur_bit_b == 1:
                    num_flip += 1
            else:
                num_flip += 1

        return num_flip


print(MinFlipsSolution(1, 2, 3).solve())
