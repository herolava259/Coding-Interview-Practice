'''
Your task is to count the number of ways you can fill an n \times m grid using 1 \times 2 and 2 \times 1 tiles.
Input
The only input line has two integers n and m.
Output
Print one integer: the number of ways modulo 10^9+7.
Constraints

1 \le n \le 10
1 \le m \le 1000

Example
Input:
4 7

Output:
781
'''

from typing import List


class CountingTilingsSolution:
    def __init__(self, n: int, m: int):
        self.n: int = n
        self.m: int = m

    def solve(self) -> int:
        mod_k = 10**9 + 7

        dp: List[List[int]] = [[0] * (1 << self.n) for _ in range(self.m + 1)]

        dp[1][0] = 1

        get_bit = lambda x, k: (x >> k) & 1 == 1

        def anti_mask(msk):
            new_msk = 0
            bit_add = 1
            counter = 0
            while counter < self.n:
                if msk & 1 == 0:
                    new_msk |= bit_add
                msk >>= 1
                bit_add <<= 1
                counter += 1
            return new_msk

        for i in range(1, self.m+1):
            # horizontal tiling
            for mask in range(1 << self.n):
                for p in range(1, self.n):
                    if get_bit(mask, p-1) or get_bit(mask, p):
                        continue
                    new_mask = mask | (1 << (p-1)) | (1 << p)
                    dp[i][new_mask] = (dp[i][new_mask] + dp[i][mask]) % mod_k
            # vertical tiling of next step
            if i < self.m:
                for mask in range(1 << self.n):
                    dp[i+1][anti_mask(mask)] = dp[i][mask]

        return dp[-1][-1]