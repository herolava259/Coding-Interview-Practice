from typing import List

mod_k = 10**9 + 7


class CountGoodStringsSolution:
    def __init__(self, low: int, high: int, zero: int, one: int):

        self.low: int = low
        self.high: int = high
        self.zero: int = zero
        self.one: int = one

    def solve(self) -> int:
        dp: List[int] = [0] * (self.high+1)

        dp[self.zero] += 1
        dp[self.one] += 1

        begin = min(self.zero, self.one)

        num_way = 0

        for i in range(begin, self.high+1):

            if i >= self.zero:
                dp[i] = (dp[i] + dp[i-self.zero]) % mod_k

            if i >= self.one:
                dp[i] = (dp[i] + dp[i-self.one]) % mod_k

            if i >= self.low:
                num_way = (num_way + dp[i]) % mod_k

        return num_way

low1 = 2
high1 = 3
zero1 = 1
one1 = 2

sln = CountGoodStringsSolution(low1, high1, zero1, one1)

print(sln.solve())

