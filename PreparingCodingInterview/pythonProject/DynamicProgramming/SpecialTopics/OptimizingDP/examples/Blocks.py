from typing import List, Deque, Tuple
from collections import deque


class BlocksSolution:
    def __init__(self,n: int, k:int, arr:List[int]):

        self.n: int = n
        self.k: int = k
        self.arr: List[int] = arr


    def base_solve(self) -> int:

        dp: List[List[int]] = [[10**9+7] * (self.n+1) for _ in range(self.k+1)]
        dp[1][0] = 0
        for i in range(1, self.k):
            for j in range(1, self.n):
                dp[i][j] = min(dp[i-1][k] + max(self.arr[k:j]) for k in range(j))

        return dp[-1][-1]

    def stack_solve(self) -> int:
        dp: List[List[int]] = [[10 ** 9 + 7] * (self.n + 1) for _ in range(self.k + 1)]

        dp[1][0] = 0

        for i in range(1, self.n+1):
            dp[1][i] = max(dp[1][i-1], self.arr[i])

        for i in range(2, self.k+1):

            st: Deque[Tuple[int, int]] = deque()

            for j in range(i, self.n+1):
                min_dp = dp[i-1][j-1]

                while st and self.arr[st[-1][1]] <= self.arr[i]:
                    min_dp = min(min_dp, st.pop()[0])

                dp[i][j] = min(dp[i][st[-1][1] if st else 0], min_dp + self.arr[j])
                st.append((min_dp, j))

        return dp[-1][-1]

