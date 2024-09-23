from typing import List


class CountBitsSolution:

    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> List[int]:

        res: List[int] = [0] * (self.n + 1)

        for i in range(1, self.n + 1):
            bit_num = res[i - 1]

            bit_seq = i - 1

            while (bit_seq & 1) == 1:
                bit_num -= 1
                bit_seq = bit_seq >> 1

            res[i] = bit_num + 1

        return res


print(CountBitsSolution(255).solve())
