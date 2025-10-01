from typing import List


class TransformingIncreasedArraySolution:
    def __init__(self, arr: List[int]):

        self.arr: List[int] = arr

    def solve(self) -> int:
        n = len(self.arr)
        arr: List[int] = [self.arr[i] - i for i in range(len(self.arr))]

        limit_k = max(arr) - min(arr) + 1

        dp: List[List[int]] = [[10**9 + 7] * limit_k for _ in range(n+1)]

        for i in range(limit_k):
            dp[1][i] = abs(arr[0] - i)

        for i in range(2, n+1):
            for j in range(limit_k):
                dp[i][j] = min(dp[i-1][k] + abs(arr[i] - k) for k in range(j+1))

        return dp[n][-1]

    def slope_solve(self) -> int:
        n = len(self.arr)
        arr: List[int] = [self.arr[i] - i for i in range(len(self.arr))]

        return len(self.arr)
