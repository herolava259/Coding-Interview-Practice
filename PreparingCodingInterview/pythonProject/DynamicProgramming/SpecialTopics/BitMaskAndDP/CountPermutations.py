"""
Given N and K, count number of permutations of [1, 2, 3...N] in which no two adjacent elements differ by more than K. For example, permutation [4, 1, 2, 3] cannot be counted for .

Input
First line contains T(1 ≤ T ≤ 10), the number of test cases. Each test case consists of N(1 ≤ N ≤ 15) and K(0 ≤ N) in single line.

Output
For each test case print the required answer in one line.
"""
from bitarray import bitarray
from typing import List

class CountPermutationSolution:
    def __init__(self, n: int, k: int):
        self.n: int = n
        self.k: int = k

    def solve(self) -> int:
        def get_bit(x: int, k: int)-> bool:
            return (x >> k) & 1 == 1

        max_n = (1 << self.n) + 1
        dp: List[List[int]] = [[0] * 16 for _ in range(max_n)]

        dp[0][0] = 1

        for mask in range(1 << self.n):
            for q in range(1, self.n+1):
                if get_bit(mask, q-1):
                    continue

                for g in range(self.n+1):
                    if g != 0 and abs(q-g) > self.k:
                        continue

                    new_mask = mask | (1 < (q-1))

                    dp[new_mask][q] += dp[mask][g]

        return sum(dp[(1 << self.n)-1])



