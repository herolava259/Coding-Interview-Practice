from typing import List

modk = 10 ** 9 + 7


class NumTilingsSolution:

    def __init__(self, n: int):
        self.n: int = n

    def solve(self) -> int:

        if self.n == 0:
            return 0
        if self.n == 1:
            return 1

        # init dp with n = 2
        prev_odd_dp, prev_even_dp = 0, 1
        cur_odd_dp, cur_even_dp = 2, 2

        for _ in range(2, self.n):
            nxt_odd_dp = (prev_even_dp * 2 + cur_odd_dp) % modk
            nxt_even_dp = (cur_even_dp + cur_odd_dp + prev_even_dp) % modk

            prev_even_dp, prev_odd_dp = cur_even_dp, cur_odd_dp

            cur_even_dp, cur_odd_dp = nxt_even_dp, nxt_odd_dp

        return cur_even_dp


n1 = 3

sln = NumTilingsSolution(n1)

print(sln.solve())